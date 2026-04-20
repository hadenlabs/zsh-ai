## 1. Project Setup

- [x] 1.1 Create the `hadx-opencode-sync` command file in the project
- [x] 1.2 Add the command to the project exports/loading mechanism

## 2. Core Functionality

- [x] 2.1 Implement function to read `opencode.json` and extract plugins
- [x] 2.2 Implement function to create `docs/opencode/plugins` directory if not exists
- [x] 2.3 Implement Markdown generation for each plugin
- [x] 2.4 Implement standard documentation format template

## 3. Dry-Run Mode

- [x] 3.1 Add `--dry-run` flag parsing
- [x] 3.2 Implement preview output showing planned changes without file modification

## 4. Diff Display

- [x] 4.1 Implement diff generation between current and proposed state
- [x] 4.2 Display diff output before applying changes

## 5. Manual Change Protection

- [x] 5.1 Implement detection of manual changes (marker comments or file content comparison)
- [x] 5.2 Add warning output when manual changes are detected
- [x] 5.3 Implement confirmation prompt before overwriting manual changes
- [x] 5.4 Implement skip option for files with manual changes

## 6. Testing

- [x] 6.1 Test command with sample `opencode.json`
- [x] 6.2 Test `--dry-run` mode
- [x] 6.3 Test diff display
- [x] 6.4 Test manual change protection

## 7. Documentation

- [x] 7.1 Add command documentation to project docs
- [x] 7.2 Add usage examples