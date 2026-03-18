"""CLI for audio-intelligence-platform."""
import sys, json, argparse
from .core import AudioIntelligencePlatform

def main():
    parser = argparse.ArgumentParser(description="Audio analysis platform — transcription, speaker ID, sentiment, music understanding")
    parser.add_argument("command", nargs="?", default="status", choices=["status", "run", "info"])
    parser.add_argument("--input", "-i", default="")
    args = parser.parse_args()
    instance = AudioIntelligencePlatform()
    if args.command == "status":
        print(json.dumps(instance.get_stats(), indent=2))
    elif args.command == "run":
        print(json.dumps(instance.process(input=args.input or "test"), indent=2, default=str))
    elif args.command == "info":
        print(f"audio-intelligence-platform v0.1.0 — Audio analysis platform — transcription, speaker ID, sentiment, music understanding")

if __name__ == "__main__":
    main()
