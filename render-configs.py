import os
import re

def main():
    env_path = ".env"
    if not os.path.exists(env_path):
        print(f"Error: {env_path} not found")
        exit(1)

    env_vars = {}
    with open(env_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                env_vars[key.strip()] = value.strip()

    required_vars = ["MTG_SECRET_1", "MTG_SECRET_2", "MTG_SECRET_3"]
    missing = [v for v in required_vars if v not in env_vars or not env_vars[v]]
    if missing:
        print(f"Error: Missing required environment variables in {env_path}: {', '.join(missing)}")
        exit(1)

    templates_dir = "templates"
    generated_dir = "generated"

    if not os.path.exists(generated_dir):
        os.makedirs(generated_dir)

    for i in range(1, 4):
        tpl_path = os.path.join(templates_dir, f"config-{i}.toml.tpl")
        out_path = os.path.join(generated_dir, f"config-{i}.toml")

        if not os.path.exists(tpl_path):
            print(f"Error: Template {tpl_path} not found")
            continue

        with open(tpl_path, "r") as f:
            content = f.read()

        # Simple replacement
        for key, value in env_vars.items():
            content = content.replace(f"${{{key}}}", value)

        # Check if all placeholders are replaced
        remaining_placeholders = re.findall(r"\${[A-Z0-9_]+}", content)
        if remaining_placeholders:
            print(f"Warning: Not all placeholders were replaced in {out_path}: {remaining_placeholders}")

        with open(out_path, "w") as f:
            f.write(content)

        os.chmod(out_path, 0o600)
        print(f"Generated {out_path} with 0600 permissions")

if __name__ == "__main__":
    main()
