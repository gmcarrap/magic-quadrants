# Service Implementation

Flask Application for Magic Quadrants

This application provides endpoints and forms to calculate and display magic quadrants based on a given parameter N.

Endpoints:
- `/magic-quadrants-json`: Accepts JSON input to calculate magic quadrants.
- `/magic-quadrants`: Renders an HTML form to input N and displays magic quadrants.

Functions:
- `get_magic_quadrants`: Endpoint to calculate magic quadrants from JSON input.
- `magic_quadrants_form`: Endpoint to render HTML form for inputting N and displaying magic quadrants.


::: api_server