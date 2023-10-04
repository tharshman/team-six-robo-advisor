from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram("Container diagram for Toy Robo-advisor project", direction="TB", graph_attr=graph_attr) as diag:
    customer = Person(
        name="Retirement Customer",
        description="A customer interested in reviewing retirement portfolio allocations"
    )

    with SystemBoundary("Toy Robo-advisor"):
        chatbot = Container(
            name="Robo-Advisor",
            technology="Python",
            description="Robo-Advisor providing portfolio distributions based on age and sex"
        )

    customer >> Relationship("Interacts with") >> chatbot
