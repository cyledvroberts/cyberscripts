SafeDelete (delc.pl)

delc.pl is an interactive Perl script designed to safely delete files and directories specified via command-line arguments. It prompts for confirmation before deleting each item, helping to avoid accidental removals.
Features

    Accepts files and directories as command-line arguments.

    Identifies each item and prompts the user before deletion.

    Option to cancel the process at any time.

    Prevents deletion of the script itself.

    Final confirmation before proceeding with deletions.

Usage

perl delc.pl <file_or_directory> [more_files_or_directories...]

Example

perl delc.pl old_log.txt test_dir/

For each item, you will be prompted:

    Type y to mark the item for deletion.

    Type q to quit the process early.

Once all items are reviewed, a final confirmation is requested to proceed with the deletions.
Requirements

    Perl

    File::Path module (for rmtree)

    Cwd module (standard in Perl)

Safety Notes

    The script explicitly avoids deleting itself (delc.pl) regardless of its location.

    Files and directories are only deleted after all confirmations and final approval.