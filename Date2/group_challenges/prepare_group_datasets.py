from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parent
builder = ROOT / "_package_builder.py"
namespace = runpy.run_path(str(builder))
results = namespace["create_group_data"](ROOT, ROOT.parent / "outputs")
print("Regenerated group data packages:")
for group, summary in results.items():
    print(f"- {group}: {summary['rows']} primary input rows; indicators={summary['indicators']}")
