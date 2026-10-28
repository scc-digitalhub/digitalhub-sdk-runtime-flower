import subprocess
import sys
import textwrap


def test_importing_runtime_defers_pip_internals() -> None:
    script = textwrap.dedent(
        """
        import sys

        import digitalhub_runtime_flower

        loaded = [
            name
            for name in sys.modules
            if name == "pip._internal" or name.startswith("pip._internal.")
        ]
        assert not loaded, f"Unexpected pip internals: {loaded}"
        """
    )
    result = subprocess.run(
        [sys.executable, "-c", script],
        capture_output=True,
        check=False,
        text=True,
    )

    assert result.returncode == 0, result.stderr


def test_requirements_file_is_parsed_on_demand(tmp_path) -> None:
    from digitalhub_runtime_flower.entities._commons.requirement_parser.parser import RequirementParser

    requirements_file = tmp_path / "requirements.txt"
    requirements_file.write_text("requests>=2\n", encoding="utf-8")

    assert RequirementParser().parse(str(requirements_file)) == ["requests>=2"]
