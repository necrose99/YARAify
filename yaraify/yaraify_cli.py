import sys
import upload_yara_rule
import yaraify_check_taskid
import yaraify_list_tasks
import yaraify_lookup_hash
import yaraify_lookup_yara_rule
import yaraify_rescan
import yaraify_submit

COMMANDS = {
    "submit": yaraify_submit.main,
    "lookup": yaraify_lookup_hash.main,
    "rescan": yaraify_rescan.main,
    "upload-rule": upload_yara_rule.main,
    "check-task": yaraify_check_taskid.main,
    "list-tasks": yaraify_list_tasks.main,
    "lookup-rule": yaraify_lookup_yara_rule.main,
}

def main():
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print("Usage: yaraify-cli <command> [options]")
        print(f"Available commands: {', '.join(COMMANDS.keys())}")
        sys.exit(1)

    # Shift arguments so submodules process sys.argv natively
    cmd = sys.argv.pop(1)
    COMMANDS[cmd]()

if __name__ == "__main__":
    main()
