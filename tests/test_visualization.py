import os
from src.visualization import create_all_cases_graph, create_one_case_graph
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def test_visualization_all():
    """
    tests create_all_cases_graph
    """
    create_all_cases_graph([2,3], figure_path=os.path.join(CURRENT_DIR,"figures"))
    assert os.path.isfile(f"{CURRENT_DIR}/figures/2Ck.png")
    assert os.path.isfile(f"{CURRENT_DIR}/figures/3Ck.png")
    os.remove(f"{CURRENT_DIR}/figures/2Ck.png")
    os.remove(f"{CURRENT_DIR}/figures/3Ck.png")

def test_visualization_one():
    """
    tests create_one_case_graph
    """
    n=25
    create_one_case_graph(n, 1, figure_path=os.path.join(CURRENT_DIR,"figures"))
    create_one_case_graph(n,12, figure_path=os.path.join(CURRENT_DIR,"figures"))
    create_one_case_graph(n, 24, figure_path=os.path.join(CURRENT_DIR,"figures"))
    n=24
    create_one_case_graph(n, 1, figure_path=os.path.join(CURRENT_DIR,"figures"))
    create_one_case_graph(n,12, figure_path=os.path.join(CURRENT_DIR,"figures"))
    create_one_case_graph(n, 23, figure_path=os.path.join(CURRENT_DIR,"figures"))
    assert os.path.isfile(f"{CURRENT_DIR}/figures/25_1_alone.png")
    assert os.path.isfile(f"{CURRENT_DIR}/figures/25_12_alone.png")
    assert os.path.isfile(f"{CURRENT_DIR}/figures/25_24_alone.png")
    assert os.path.isfile(f"{CURRENT_DIR}/figures/24_1_alone.png")
    assert os.path.isfile(f"{CURRENT_DIR}/figures/24_12_alone.png")
    assert os.path.isfile(f"{CURRENT_DIR}/figures/24_23_alone.png")
    os.remove(f"{CURRENT_DIR}/figures/25_1_alone.png")
    os.remove(f"{CURRENT_DIR}/figures/25_12_alone.png")
    os.remove(f"{CURRENT_DIR}/figures/25_24_alone.png")
    os.remove(f"{CURRENT_DIR}/figures/24_1_alone.png")
    os.remove(f"{CURRENT_DIR}/figures/24_12_alone.png")
    os.remove(f"{CURRENT_DIR}/figures/24_23_alone.png")
