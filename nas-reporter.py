#!/usr/bin/env python3

import argparse
import smtplib

def send_email(dest_mx, toaddrs, fromaddr, subject, content):
    msg = f"From: {fromaddr}\r\nTo: %{toaddrs}\r\n"

    msg += f"Subject: {subject}\r\n\r\n"
    msg += content

    print("Message length is", len(msg))

    server = smtplib.SMTP(dest_mx)
    server.set_debuglevel(1)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="verbose output", action="store_true")
    args = parser.parse_args()
    
    if args.verbose:
        print("Verbosity turned on.")


if __name__ == '__main__':
    main()
