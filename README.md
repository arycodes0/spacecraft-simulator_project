# Spacecraft Simulator

A software-only spacecraft subsystem simulator for exploring power, temperature, telemetry, and mission operations.

The project starts with Python checks for battery level and temperature. The planned application will simulate a spacecraft over time and provide a browser-based mission-control dashboard for observing telemetry, issuing commands, and investigating faults.

**Status: early prototype.** Only the battery and temperature checks described below are currently implemented. The simulation engine, API, dashboard, and storage are planned.

## Scope

All spacecraft behavior and sensor readings will be generated in software. No physical sensors, microcontrollers, or other hardware are required.

The initial goal is to model one spacecraft with:

- Battery storage, solar generation, and electrical loads.
- Temperature changes and heater operation.
- Sunlight and eclipse conditions.
- Normal and safe operating modes.
- Telemetry, alerts, commands, and injected faults.

Orbital mechanics and 3D visualization are possible later extensions. The initial models will use simplified, documented assumptions for learning and experimentation.

## Current features

| Module | Function | Behavior |
| --- | --- | --- |
| `battery.py` | `check_battery(battery_percent)` | Returns `"LOW BATTERY"` when the value is between 0 and 30, inclusive; otherwise returns `""`. |
| `temperature.py` | `check_temperature(temperature_c)` | Returns `"HIGH TEMPERATURE"` above 50°C; otherwise returns `""`. |

These functions evaluate supplied values; they do not generate telemetry or advance a simulation. Input validation is not yet implemented. In particular, battery values below 0 or above 100 currently return an empty string.

## Getting started

### Requirements

- Python 3.10 or newer is recommended.
- Git to clone the repository.

The current modules use only the Python standard library. No third-party packages or hardware connections are needed.

### Clone the repository

```bash
git clone https://github.com/arycodes0/spacecraft-simulator_project.git
cd spacecraft-simulator_project
```

### Try the checks

Start Python from the repository root:

```bash
python
```

On systems where Python is installed as `python3`, use that command instead.

```python
from battery import check_battery
from temperature import check_temperature

print(check_battery(25))       # LOW BATTERY
print(check_battery(30))       # LOW BATTERY
print(repr(check_battery(80))) # ''

print(check_temperature(55))       # HIGH TEMPERATURE
print(repr(check_temperature(50))) # ''
```

There is currently no application entry point, web server, or dashboard to launch. Running the module files directly does not display a simulation.

## Current repository structure

```text
spacecraft-simulator_project/
├── README.md
├── battery.py
└── temperature.py
```

## Proposed technology stack

The following stack is a development recommendation; these dependencies have not yet been integrated.

| Layer | Technology | Purpose |
| --- | --- | --- |
| Simulation | Python; NumPy/SciPy as needed | State updates, power and thermal models, numerical calculations |
| API | FastAPI + Pydantic | Validated commands, configuration, and state endpoints |
| Live telemetry | WebSockets | Stream simulation updates to the dashboard |
| Frontend | React + TypeScript + Vite | Interactive mission-control interface |
| Styling and charts | Tailwind CSS + Recharts | Status panels, controls, and telemetry plots |
| Persistence | SQLite + SQLAlchemy | Scenarios, events, commands, and run summaries |
| Quality | pytest + Ruff; Vitest + Playwright | Model validation, code checks, and UI workflows |
| Tooling | uv, npm, GitHub Actions | Dependency management and automated checks |
| Packaging | Docker Compose | Run the application components together when ready |

Start with one backend, one frontend, and a local SQLite database. Add infrastructure only when concrete requirements justify it.

## Planned architecture

```text
Scenario configuration ──> Python simulation engine
                                   │
                            State and alerts
                                   │
                              FastAPI API ──> Saved run data
                                   │
                         WebSocket telemetry
                                   │
                            React dashboard
                                   │
                           Commands via API
                                   │
                                   └────────> Simulation engine
```

The simulation engine will own the spacecraft state. The dashboard will display telemetry and submit validated commands through the API.

Simulation time will advance in fixed steps independently of dashboard rendering or real-world time. This enables pause, single-step, accelerated playback, and reproducible runs. Configuration, random seed, timestep, model version, and scheduled commands will be recorded for reproducibility.

## Development roadmap

1. **Define the first scenario.** Document spacecraft parameters, units, commands, model assumptions, and success conditions. Use an eclipse-and-recovery scenario as the first milestone.
2. **Structure the Python core.** Introduce state, configuration, command, and alert models. Make thresholds configurable and reject invalid inputs. Test the battery and temperature boundaries.
3. **Build the simulation loop.** Add start, pause, reset, and single-step controls. Use a fixed timestep and seeded randomness where needed.
4. **Implement power and thermal behavior.** Update battery energy from generation minus consumption over elapsed time. Model sunlight, eclipse, equipment heat, and heaters. Keep units explicit and validate behavior against simple reference cases.
5. **Add operating modes and faults.** Support payload switching, heater control, safe mode, solar-panel failure, and sensor faults. Separate simulated physical state from sensor readings. Add alert clearing rules and hysteresis to prevent rapid toggling near thresholds.
6. **Expose an API.** Add configuration, state, command, and run-control endpoints, plus WebSocket telemetry. Begin with one active simulation session and serialize state changes.
7. **Build the dashboard.** Display subsystem status, charts, active alerts, an event log, simulation time, connection status, and command controls.
8. **Persist and export runs.** Save configurations, commands, events, and summaries. Export telemetry as CSV or JSON; record telemetry for exact visual playback.
9. **Validate and package.** Add automated checks, setup instructions, and an end-to-end scenario test. Package the application for a repeatable local demo.
10. **Explore extensions.** Consider orbital dynamics, position-derived eclipse periods, additional subsystems, and 3D visualization after the core simulation is validated.

### First milestone: eclipse and recovery

A complete first demo should show this sequence:

1. The spacecraft starts in sunlight with a charged battery.
2. Eclipse removes solar generation, and electrical loads drain the battery.
3. Battery and temperature telemetry update over simulated time.
4. Low charge triggers an alert.
5. Entering safe mode reduces electrical consumption.
6. Returning to sunlight restores charging and eventually clears the alert according to its configured clearing threshold.

**Acceptance criteria:** the scenario can run through the dashboard, commands and alerts appear in the event log, battery energy stays within physical limits, and identical recorded inputs reproduce the same simulation history.

## Validation plan

An automated test suite has not yet been added. Planned checks include:

- Battery and temperature threshold boundaries, plus invalid input handling.
- Power accounting, battery capacity limits, and documented thermal reference cases.
- Deterministic runs with identical configuration, seed, and command timing.
- Command validation, operating-mode transitions, and alert activation/clearing.
- An end-to-end eclipse, alert, safe-mode, and recovery workflow.

## Contributing

Open an issue to discuss substantial changes, or submit a focused pull request. For simulation changes, document assumptions and units, include a reproducible scenario, and add tests for the affected behavior. Keep documentation clear about implemented features and future plans.

## License

No license file is currently included in the repository. A license should be selected and added before granting reuse or redistribution rights.
