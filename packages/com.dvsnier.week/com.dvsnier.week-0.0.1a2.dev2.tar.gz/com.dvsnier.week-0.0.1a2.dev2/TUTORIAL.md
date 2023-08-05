# Tutorial

- [Introduce](#introduce)
  - [CLI](#cli)

## Introduce

this is week modules.

### CLI

```bash
usage: dvs-week [-h] [-V] [-cp current-project] [-pp project-prefix] [-dp [dest-project]] [-dpl dest-project-list [dest-project-list ...]]
                [-pcl project-config-list [project-config-list ...]] [-escf email-ssl-config-file] [-nf note-flavor] [-s since] [-u until] [-lm [latest-month]]
                [-lw [latest-week]] [-author [author]] [-authors authors [authors ...]] [-subject subject] [-f flags]
                [-tal target-absolute-list [target-absolute-list ...]] [-el [exclude-list [exclude-list ...]]] [-iar] [-dr] [-uslgr] [-rsrbl] [-s2]

    this is a dvs week execution program.

        program one step: the update or synchronization local git repository

            the Notice:

                1. the only absolute path fields are supported

                    target_absolute_list = ['/User/.../xxx', '/User/.../yyy', '/User/.../zzz']

                2. the custom exclusion lists are currently supported

                    exclude_list = ['...', '...']

                3. the is associate remote are currently supported

                    iar = False

                4. the uslgr are currently supported

                    uslgr = True

        program two step: the recent specific range branch list

            the Notice:

                1. the dest-project are currently supported

                    dest-project = ...

                2. the dict are currently supported

                    - kwargs is dict {
                        'since' : '2021-07-01',
                        'until' : '2021-07-31',
                        'latest-month' : [1-12],
                        'latest-week' : [1-4],
                        'flags' : [0|1|2|3]
                      }

                    the please notice:

                        - The kwargs{since, until} and kwargs{latest_month, latest_week} are mutually exclusive options;
                        - since and until that both must exist at the same time
                        - (since, until) and latest_month and latest_week parameters,
                          All three are optional, but you must choose one of them.

                3. the email ssl config file are currently supported

                    email-ssl-config-file = ...

                4. the rsrbl are currently supported

                    rsrbl = True

        program three step: the statistical summary commit recorder information

                1. the destination project list are currently supported

                    dest-project-list = ['/User/.../xxx', '/User/.../yyy', '/User/.../zzz']

                2. the since are currently supported

                    since = '2021-07-01'

                3. the until are currently supported

                    until = '2021-07-31'

                4. the flags are currently supported

                    flags = [0|1|2|3]

                    the please notice:

                        - 0: remotes
                        - 1: locals
                        - 2: locals and specific range
                        - 3: remotes and specific range

                5. the email ssl config file are currently supported

                    email-ssl-config-file = ...

                6. the note-flavor are currently supported

                    note-flavor = [d, w, m, y]

                7. the s2 are currently supported

                    s2 = True


optional arguments:
  -h, --help            show this help message and exit
  -V, --version         the show version and exit.
  -cp current-project, --current-project current-project
                        the dvs current project property.
  -pp project-prefix, --project-prefix project-prefix
                        the dvs project prefix property.
  -dp [dest-project], --dest-project [dest-project]
                        the dest project property.
  -dpl dest-project-list [dest-project-list ...], --dest-project-list dest-project-list [dest-project-list ...]
                        the dest project list property.
  -pcl project-config-list [project-config-list ...], --project-config-list project-config-list [project-config-list ...]
                        the project config list property.
  -escf email-ssl-config-file, --email-ssl-config-file email-ssl-config-file
                        the email ssl config file.
  -nf note-flavor, --note-flavor note-flavor
                        The note flavor spatial range of the week can only be the following values: [d, w, m, y] and the default value is week.
  -s since, --since since
                        the since property that is format with YY-mm-dd.
  -u until, --until until
                        the until property that is format with YY-mm-dd.
  -lm [latest-month], --latest-month [latest-month]
                        The latest month spatial range of the week can only be the following values: [1, 12] and the default value is zero with no execute.       
  -lw [latest-week], --latest-week [latest-week]
                        The latest week spatial range of the week can only be the following values: [1, 4] and the default value is zero with no execute.
  -author [author], --author [author]
                        the author property.
  -authors authors [authors ...], --authors authors [authors ...]
                        the authors property.
  -subject subject, --subject subject
                        the subject property.
  -f flags, --flags flags
                        The flags spatial range of the week can only be the following values: {0, 1, 2, 3} that is 0: remotes 1: locals 2: locals and specific    
                        range 3: remotes and specific range and the default value is zero.
  -tal target-absolute-list [target-absolute-list ...], --target-absolute-list target-absolute-list [target-absolute-list ...]
                        the target absolute list property.
  -el [exclude-list [exclude-list ...]], --exclude-list [exclude-list [exclude-list ...]]
                        the exclude list property.
  -iar, --is-associate-remote
                        if iar == true, update or synchronization remote git repository, otherwise only local repository it.
  -dr, --dry-run        if dr == true, the skip execute program, otherwise no it.
  -uslgr, --update-or-synchronization-local-git-repository
                        if uslgr == true, update or synchronization local git repository, otherwise no it.
  -rsrbl, --recent-specific-range-branch-list
                        if rsrbl == true, recent specific range branch list, otherwise no it.
  -s2, --statistical-summary
                        if s2 == true, do statistical summary data, otherwise no it.

the copyright belongs to DovSnier that reserve the right of final interpretation.
```
