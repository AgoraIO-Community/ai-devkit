#!/usr/bin/env node
/**
 * Record the presentation player as an MP4 video.
 *
 * Usage:
 *   node record.mjs [--fps 10] [--width 1920] [--height 1080] [--duration 30] [--start 60]
 *
 * --duration limits recording to N seconds (for testing). Omit for full recording.
 * --start begins recording at N seconds into the presentation (for testing). Default: 0.
 */

import { chromium } from 'playwright';
import { spawn } from 'child_process';
import { mkdirSync, rmSync, existsSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

const args = process.argv.slice(2);
function getArg(name, def) {
  const idx = args.indexOf(`--${name}`);
  return idx >= 0 && args[idx + 1] ? args[idx + 1] : def;
}

const CAPTURE_FPS = Number(getArg('fps', 10));
const OUTPUT_FPS = 30;
const WIDTH = Number(getArg('width', 1920));
const HEIGHT = Number(getArg('height', 1080));
const MAX_DURATION = getArg('duration', null);
const START_TIME = Number(getArg('start', 0));
const BASE_URL = 'http://localhost:8090/player.html';
const FRAMES_DIR = join(__dirname, 'frames');
const RUNS_DIR = join(__dirname, 'runs');

// Generate datetime-stamped output filename
function outputPath() {
  const now = new Date();
  const yyyy = now.getFullYear();
  const mm = String(now.getMonth() + 1).padStart(2, '0');
  const dd = String(now.getDate()).padStart(2, '0');
  const hh = String(now.getHours()).padStart(2, '0');
  const min = String(now.getMinutes()).padStart(2, '0');
  mkdirSync(RUNS_DIR, { recursive: true });
  return join(RUNS_DIR, `ai-devkit-overview-${yyyy}-${mm}-${dd}_${hh}${min}.mp4`);
}
const OUTPUT = getArg('output', null) || outputPath();

async function main() {
  if (existsSync(FRAMES_DIR)) rmSync(FRAMES_DIR, { recursive: true });
  mkdirSync(FRAMES_DIR, { recursive: true });

  console.log(`Recording at ${WIDTH}x${HEIGHT} @ ${CAPTURE_FPS}fps capture → ${OUTPUT_FPS}fps output`);
  if (MAX_DURATION) console.log(`Limited to ${MAX_DURATION}s`);
  if (START_TIME) console.log(`Starting at ${START_TIME}s`);

  const browser = await chromium.launch({
    headless: true,
    args: ['--disable-gpu', '--no-sandbox'],
  });

  const context = await browser.newContext({
    viewport: { width: WIDTH, height: HEIGHT },
    deviceScaleFactor: 1,
  });

  const page = await context.newPage();

  console.log('Loading player...');
  await page.goto(BASE_URL, { waitUntil: 'networkidle' });
  await page.waitForTimeout(3000); // Let fonts, SVG, audio metadata load

  // Get audio duration and verify data loaded
  const info = await page.evaluate(() => {
    const audio = document.getElementById('audio');
    return {
      duration: audio.duration,
      timingCount: combinedTiming.length,
      enSubCount: subtitlesEn.length,
      zhSubCount: subtitlesZh.length,
    };
  });

  console.log(`Audio duration: ${info.duration.toFixed(1)}s`);
  console.log(`Timing entries: ${info.timingCount}, EN subs: ${info.enSubCount}, ZH subs: ${info.zhSubCount}`);

  const TITLE_HOLD = 2; // seconds of silence before audio starts on title slide
  const TITLE_AUDIO = 3; // seconds of audio to play while still showing title slide (Hello and welcome)
  const CLOSING_HOLD = 4; // seconds to show closing slide after audio ends
  const endTime = MAX_DURATION ? Math.min(START_TIME + Number(MAX_DURATION), info.duration) : info.duration;
  const recordDuration = endTime - START_TIME;
  const titleFrames = Math.ceil(TITLE_HOLD * CAPTURE_FPS);
  const audioFrames = Math.ceil(recordDuration * CAPTURE_FPS);
  const closingFrames = Math.ceil(CLOSING_HOLD * CAPTURE_FPS);
  const totalFrames = titleFrames + audioFrames + closingFrames;
  console.log(`Title hold: ${TITLE_HOLD}s (${titleFrames} frames)`);
  console.log(`Audio frames: ${audioFrames} (${recordDuration.toFixed(1)}s, from ${START_TIME}s to ${endTime.toFixed(1)}s)`);
  console.log(`Closing hold: ${CLOSING_HOLD}s (${closingFrames} frames)`);
  console.log(`Total frames to capture: ${totalFrames}`);

  // Set up recording mode: switch to play mode, mute audio, disable rAF loop
  await page.evaluate(() => {
    const audio = document.getElementById('audio');
    audio.muted = true;
    audio.pause();

    // Switch to playing mode so subtitle panel is visible (not transcript panel)
    document.body.classList.remove('browse');
    document.body.classList.add('playing');

    // Kill the rAF loop so it doesn't interfere
    window.__origRAF = window.requestAnimationFrame;
    window.requestAnimationFrame = () => {};
  });

  // Capture title slide frames (silent hold)
  let lastPct = -1;
  let frameNum = 0;

  // Show title slide (slide 1) with no subtitles
  await page.evaluate(() => {
    document.querySelectorAll('.slide').forEach(s => s.classList.remove('active'));
    const title = document.querySelector('.slide[data-slide="1"]');
    if (title) title.classList.add('active');
    document.getElementById('slideIndicator').textContent = '1 / 10';
    document.getElementById('subtitleEn').textContent = '';
    document.getElementById('subtitleZh').textContent = '';
    document.getElementById('progressFill').style.width = '0%';
    document.getElementById('timeDisplay').textContent = '0:00 / 0:00';
  });

  console.log(`Capturing ${titleFrames} title slide frames...`);
  for (let i = 0; i < titleFrames; i++) {
    const framePath = join(FRAMES_DIR, `frame-${String(frameNum).padStart(6, '0')}.png`);
    await page.screenshot({ path: framePath, type: 'png' });
    frameNum++;

    const pct = Math.floor((frameNum / totalFrames) * 100);
    if (pct !== lastPct && pct % 5 === 0) {
      lastPct = pct;
      process.stdout.write(`\rCapturing: ${pct}% (${frameNum}/${totalFrames}) title`);
    }
  }

  // Capture audio-driven frames
  for (let i = 0; i < audioFrames; i++) {
    const currentTime = START_TIME + (i / CAPTURE_FPS);

    // Drive the entire UI state in one evaluate call
    await page.evaluate(({t, titleAudio}) => {
      const audio = document.getElementById('audio');

      // 1. Set the time
      audio.currentTime = t;

      // 2. Progress bar
      const dur = audio.duration || 1;
      document.getElementById('progressFill').style.width = `${(t / dur) * 100}%`;

      // 3. Time display
      const fm = (s) => {
        const m = Math.floor(s / 60);
        const sec = Math.floor(s % 60);
        return `${m}:${sec.toString().padStart(2, '0')}`;
      };
      document.getElementById('timeDisplay').textContent = `${fm(t)} / ${fm(dur)}`;

      // 4. Current slide
      // During first titleAudio seconds, keep title slide (1) visible
      // After that, JSON slides 1-8 map to display slides 2-9
      let displaySlide;
      if (t < titleAudio) {
        displaySlide = 1; // title slide stays during greeting
      } else {
        let jsonSlide = 1;
        for (let j = combinedTiming.length - 1; j >= 0; j--) {
          if (t >= combinedTiming[j].offset) {
            jsonSlide = combinedTiming[j].slide;
            break;
          }
        }
        displaySlide = jsonSlide + 1; // offset by 1 for title slide
      }

      // Show closing slide (10) when "Goodbye" subtitle starts
      const goodbyeSub = subtitlesEn.find(s => s.text.startsWith('Goodbye'));
      if (goodbyeSub && t >= goodbyeSub.start) {
        displaySlide = 10;
      }

      const totalSlides = 10;
      document.getElementById('slideIndicator').textContent =
        `${displaySlide} / ${totalSlides}`;

      // 5. English subtitle — extend end time by 0.8s so text lingers
      const SUB_LINGER = 0.8;
      const enSub = subtitlesEn.find(s => t >= s.start && t <= s.end + SUB_LINGER);
      document.getElementById('subtitleEn').textContent = enSub ? enSub.text : '';

      // 6. Chinese subtitle
      const zhSub = subtitlesZh.find(s => t >= s.start && t <= s.end + SUB_LINGER);
      document.getElementById('subtitleZh').textContent = zhSub ? zhSub.text : '';

      // 7. Switch active slide
      document.querySelectorAll('.slide').forEach(s => s.classList.remove('active'));
      const target = document.querySelector(`.slide[data-slide="${displaySlide}"]`);
      if (target) target.classList.add('active');
    }, {t: currentTime, titleAudio: TITLE_AUDIO});

    // Screenshot
    const framePath = join(FRAMES_DIR, `frame-${String(frameNum).padStart(6, '0')}.png`);
    await page.screenshot({ path: framePath, type: 'png' });
    frameNum++;

    const pct = Math.floor((frameNum / totalFrames) * 100);
    if (pct !== lastPct && pct % 5 === 0) {
      lastPct = pct;
      process.stdout.write(`\rCapturing: ${pct}% (${frameNum}/${totalFrames}) t=${currentTime.toFixed(1)}s`);
    }
  }

  // Capture closing slide frames (slide 10)
  await page.evaluate(() => {
    document.querySelectorAll('.slide').forEach(s => s.classList.remove('active'));
    const closing = document.querySelector('.slide[data-slide="10"]');
    if (closing) closing.classList.add('active');
    document.getElementById('slideIndicator').textContent = '10 / 10';
    document.getElementById('subtitleEn').textContent = '';
    document.getElementById('subtitleZh').textContent = '';
  });

  console.log(`\nCapturing ${closingFrames} closing slide frames...`);
  for (let i = 0; i < closingFrames; i++) {
    const framePath = join(FRAMES_DIR, `frame-${String(frameNum).padStart(6, '0')}.png`);
    await page.screenshot({ path: framePath, type: 'png' });
    frameNum++;

    const pct = Math.floor((frameNum / totalFrames) * 100);
    if (pct !== lastPct && pct % 5 === 0) {
      lastPct = pct;
      process.stdout.write(`\rCapturing: ${pct}% (${frameNum}/${totalFrames}) closing`);
    }
  }

  console.log(`\rCapturing: 100% (${frameNum}/${totalFrames})`);
  await browser.close();

  // Compose with ffmpeg
  console.log('\nComposing video with ffmpeg...');
  const audioPath = join(__dirname, 'audio', 'full.mp3');

  // Audio starts after TITLE_HOLD seconds of silent title frames
  const ffmpegArgs = [
    '-y',
    '-framerate', String(CAPTURE_FPS),
    '-i', join(FRAMES_DIR, 'frame-%06d.png'),
    '-ss', String(START_TIME),
    '-i', audioPath,
    '-c:v', 'libx264',
    '-preset', 'medium',
    '-crf', '18',
    '-r', String(OUTPUT_FPS),
    '-pix_fmt', 'yuv420p',
    '-c:a', 'aac',
    '-b:a', '192k',
    '-af', `adelay=${TITLE_HOLD * 1000}|${TITLE_HOLD * 1000}`,
    '-shortest',
    '-movflags', '+faststart',
    OUTPUT,
  ];

  const ffmpeg = spawn('ffmpeg', ffmpegArgs, { stdio: 'inherit' });
  await new Promise((resolve, reject) => {
    ffmpeg.on('close', (code) => code === 0 ? resolve() : reject(new Error(`ffmpeg exit ${code}`)));
  });

  console.log(`\nVideo saved to: ${OUTPUT}`);
  console.log('Cleaning up frames...');
  rmSync(FRAMES_DIR, { recursive: true });
  console.log('Done!');
}

main().catch((err) => { console.error(err); process.exit(1); });
