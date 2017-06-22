from adaption import adapt
from write_excel import expexcel

if __name__ == "__main__":
    result = adapt()
    expexcel(result.get("ADP"), result.get("ADK"), result.get("ZAP"))