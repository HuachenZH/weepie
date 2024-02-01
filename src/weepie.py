import argparse
from extract_frame import extract_frame



def get_args():
    parser = argparse.ArgumentParser(prog="Weepie")
    subparsers = parser.add_subparsers(help="sub-command help", dest="cmd_name")

    parser_extractFrames = subparsers.add_parser('extractFrames', help='a help')
    parser_extractFrames.add_argument("videoPath", help="path to the video file")
    parser.add_argument("-i", "--imageDirPath", help="path to the output directory of extracted frames", default="../data/img/")
    parser.add_argument("-freq", "--frequency", help="frequency of extracting frames", default=10)

    args = parser.parse_args()
    return args



def main():
    args = get_args()

    if args.cmd_name == "extractFrames":
        breakpoint()
        extract_frame(args.videoPath, args.imageDirPath, args.frequency)
        

    #video_path = "../data/video/csa.mp4"
    #out_dir = "../data/img/"



if __name__ == "__main__":
    main()