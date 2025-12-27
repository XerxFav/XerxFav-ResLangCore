# CI Orchestration Map

```mermaid
flowchart TD

    subgraph TESTS["Tests"]
        T1["tests.yml"]
    end

    subgraph PHASES["Phase Audits"]
        P1["arca_phases.yml"]
        P2["phase_router.yml"]
    end

    subgraph UNIVERSAL["Universal CI"]
        U1["universal-ci.yml"]
    end

    T1 --> U1
    P1 --> U1
    P2 --> U1
