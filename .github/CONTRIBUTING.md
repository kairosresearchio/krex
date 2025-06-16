# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.
Please note we have a [code of conduct](CODE_OF_CONDUCT.md), please follow it in all your interactions with the project.

## Development environment setup

1. Download uv [Official Documentation](https://docs.astral.sh/uv/getting-started/installation/)
2. Create a virtual environment:
   ```sh
   uv venv
   ```
3. Activate the virtual environment:
   - **Windows**:
     ```sh
     .venv\Scripts\activate
     ```
   - **Mac/Linux**:
     ```sh
     source .venv/bin/activate
     ```
4. Install dependencies:
   ```sh
   uv sync
   ```
5. Run the project:

   ```sh
   uv run ooo.py
   ```

6. Install git hooks:

   ```sh
   pre-commit install
   pre-commit install --hook-type commit-msg

   ```

7. Run pre commit checks on all files:
   ```sh
   pre-commit run --all-files
   ```

### Commit message rules

Consider following the below format for the commit message:

Commit Type : `build|chore|ci|docs|feat|fix|perf|refactor|revert|style|test`

> 🔔 **Note**: To trigger automatic releases via GitHub Actions, use `feat:`, `fix:`, or other release-related types. `chore:` commits will be ignored by default.

**Examples**

- feat: create a new feature.
- fix: resolve a bug.
- style: apply code style changes (e.g., formatting).

### Using Commitizen

This project uses [Commitizen](https://commitizen-tools.github.io/commitizen/) to standardize commit messages and enable automated versioning and changelog generation.

Instead of manually typing commit messages, you can run:

```sh
cz commit
```

This will guide you through an interactive prompt to compose a conventional commit message, ensuring compatibility with our release automation system.

> 💡 **Reminder**: Commit messages using `feat:`, `fix:`, or `perf:` will trigger automatic version bumps and changelog generation via GitHub Actions (`release-please`).

If you prefer to write your own commit messages, please follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) format:

```
<type>(optional-scope): description
```

**Examples:**

- `feat(auth): add OAuth2 login support`
- `fix(api): handle timeout edge case`
- `refactor: simplify data parser logic`

Releases are handled automatically via GitHub Actions and [release-please](https://github.com/googleapis/release-please), based on your commit history.

> 💡 You do not need to run `cz bump` manually — versioning and changelogs are managed automatically.

## Issues and feature requests

You've found a bug in the source code, a mistake in the documentation or maybe you'd like a new feature? You can help us by [submitting an issue on GitHub](https://github.com/kairosresearchio/krex/issues). Before you create an issue, make sure to search the issue archive -- your issue may have already been addressed!

Please try to create bug reports that are:

- _Reproducible._ Include steps to reproduce the problem.
- _Specific._ Include as much detail as possible: which version, what environment, etc.
- _Unique._ Do not duplicate existing opened issues.
- _Scoped to a Single Bug._ One bug per report.

If you have any great ideas of Feature Request, please avoid adding it to the Issues section in Github and instead [start a new Discussion on Github](https://github.com/kairosresearchio/krex/discussions/categories/ideas). This allows the maintainers and the member a common place to discuss about the Request. Make sure to check if your request or idea has already been discussed or closed to avoid duplication.

**Even better: Submit a pull request with a fix or new feature!**

### How to submit a Pull Request

1. Search our repository for open or closed [Pull Requests](https://github.com/kairosresearchio/krex/pulls) that relate to your submission. You don't want to duplicate effort.
2. Fork the project.
3. Create your feature branch (`git checkout -b feat/amazing_feature`).
4. Commit your changes (`git commit -m 'feat: add amazing_feature'`). Please follow the specification mentioned above for your commit messages.
5. Push to the branch (`git push origin feat/amazing_feature`).
6. [Open a Pull Request](https://github.com/kairosresearchio/krex/compare?expand=1).
7. Make sure to fill in the all the details in the Pull Request to make it easier for the reviewers. Make sure to refer to any discussion or Issues that your PR is fixing.
