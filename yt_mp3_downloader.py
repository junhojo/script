import subprocess
import sys
import os

# python3 yt_mp3_downloader.py "https://www.youtube.com/watch?v=TgOu00Mf3kI"
def download_youtube_audio_as_mp3(url: str, output_path: str = "music"):
    try:
        # 디렉토리가 존재하지 않으면 생성
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f"📁 디렉토리 생성: {output_path}")

        # 출력 파일 경로 템플릿
        output_template = os.path.join(output_path, '%(title)s.%(ext)s')

        print("⬇️ yt-dlp로 오디오 다운로드 중...")
        subprocess.run([
            'yt-dlp',
            '-x',                      # extract audio
            '--audio-format', 'mp3',   # convert to mp3
            '--audio-quality', '2',    # 0: 최고 품질 (320 kbps), 2: 192 kbps 정도
            '--output', output_template,
            url
        ], check=True)

        print("🎧 MP3 다운로드 및 변환 완료!")

    except subprocess.CalledProcessError as e:
        print(f"⚠️ yt-dlp 실행 중 오류 발생: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❗ 사용법: python script.py <YouTube URL>")
    else:
        youtube_url = sys.argv[1]
        download_youtube_audio_as_mp3(youtube_url)