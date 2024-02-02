import argparse
from extract_frame import extract_frame
from delete_duplicated_frames import delete_duplicated_frames



def get_args():
    parser = argparse.ArgumentParser(prog="Weepie")
    subparsers = parser.add_subparsers(help="sub-command help", dest="cmd_name")

    parser_extractFrames = subparsers.add_parser('extractFrames', help='a help')
    parser_extractFrames.add_argument("videoPath", help="path to the video file")
    parser.add_argument("-i", "--imageDirPath", help="path to the output directory of extracted frames", default="../data/img/")
    parser_extractFrames.add_argument("-freq", "--frequency", help="frequency of extracting frames", default=10)

    parser_delDupFrames = subparsers.add_parser("delDupFrames", help="Delete duplicated frames")
    parser_delDupFrames.add_argument("-t", "--threshold", help="threshold of MSE of determining similarity of two images", default=2)

    args = parser.parse_args()
    return args



def main():
    args = get_args()

    # $ python3 weepie.py extractFrames ../data/video/csa.mp4 
    if args.cmd_name == "extractFrames":
        extract_frame(args.videoPath, args.imageDirPath, args.frequency)

    if args.cmd_name == "delDupFrames":
        delete_duplicated_frames(args.imageDirPath, args.threshold)


if __name__ == "__main__":
    main()