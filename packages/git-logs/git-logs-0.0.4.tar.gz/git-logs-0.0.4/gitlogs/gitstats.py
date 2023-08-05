import subprocess
from pathlib import Path
from collections import OrderedDict
from datetime import datetime

from gitlogs.utils.bcolors import bcolors


def is_not_git() -> bool:
    """Check if git is initialized in the repository"""
    args = "git rev-parse --git-dir".split(" ")

    output = subprocess.run(
        args,
        universal_newlines=True,
        shell=False,
        stderr=subprocess.DEVNULL, # hide standard error
        stdout=subprocess.DEVNULL, # hide output 
    )
    if output.returncode == 0:
        return False
    return True


def get_logs(before: str, after: str, reverse: bool) -> list:
    """Return results of git log [args]"""

    # < day, date, author >
    args = ["git", "log", "--pretty=format:%ai,%aN"]

    commit_logs = []
    try:
        if after != "":
            args.append("--after=" + after)
        if before:
            args.append("--before=" + before)

        logs = subprocess.check_output(
            args, shell=False, universal_newlines=True
        ).split("\n")

        # Process each line
        for line in logs:
            time_stamp, author = line.split(",")
            commit_logs.append({"time_stamp": time_stamp, "author": author})

        if reverse:
            return commit_logs[::-1]

        return commit_logs

    except Exception:
        return []


def filter_logs(logs: list, author: str, frequency="month") -> dict:
    """Filter the logs based on author and frequency(day, week, month, year)"""

    commit_count_by_freq = OrderedDict()

    for commit_info in logs:
        commit_date = commit_info["time_stamp"].split(" ")[0]

        is_weekend = False
        if frequency == "week":
            # %V gives number of weeks so far in a given year
            commit_date = datetime.strptime(commit_date, "%Y-%m-%d").strftime("%Y/%V")
        elif frequency == "month":
            commit_date = commit_info["time_stamp"][:7]  # YYYY-MM
        elif frequency == "year":
            commit_date = commit_info["time_stamp"][:4]  # YYYY
        else:
            # return the day of the week
            is_weekend = (
                True
                if (datetime.strptime(commit_date, "%Y-%m-%d").weekday() > 4)
                else False
            )
            # Monday=0, Tuesday=1, Wednesday=2 and so on..

        if author != "":
            if author not in commit_info["author"]:
                continue

        if commit_date not in commit_count_by_freq:
            # Add entry for that commit date
            commit_count_by_freq[commit_date] = {
                "time_stamp": commit_info["time_stamp"],
                "commits": 0,
                "weekend": is_weekend,
            }

        # Entry already exists for that commit date so increment
        commit_count_by_freq[commit_date]["commits"] += 1
    return commit_count_by_freq


def normalize(value: int, xmin: int, xmax: int) -> float:
    """Return min-max normalized value"""
    return float(value - xmin) / float(xmax - xmin)


def get_relative_count(filtered_commits: OrderedDict) -> OrderedDict:
    """Compute normalized score/count based on given filter"""

    values = [item["commits"] for item in filtered_commits.values()]
    values.append(0)  # To handle the case where only 1 value is present

    xmin = min(values)
    xmax = max(values)

    normalized_info = OrderedDict()

    for commit_date in filtered_commits.keys():
        normalized_info[commit_date] = filtered_commits[commit_date].copy()
        # add normalized value
        normalized_info[commit_date]["score"] = normalize(
            filtered_commits[commit_date]["commits"], xmin, xmax
        )

    return normalized_info


def display(logs: OrderedDict) -> None:
    """Display commit information to stdout"""

    for commit_date in logs:
        count = str(logs[commit_date]["commits"])

        print(f"{bcolors.header(commit_date)}  {bcolors.okblue(count)}", end="\t")

        # Scale up the scores by 50x
        print(bcolors.ok("-") * int(logs[commit_date]["score"] * 50))
