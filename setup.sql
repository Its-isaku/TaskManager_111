--? Create our DB table:
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(64),
    summary varchar(128),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);

--? Create some realistic dummy data to test with:
INSERT INTO tasks (
    name,
    summary,
    description
) VALUES 
(
    'Write project proposal',
    'Draft and submit the initial project proposal',
    'Prepare a detailed project proposal document outlining objectives, timeline, and deliverables. Submit to the team lead for review.'
),
(
    'Team meeting',
    'Weekly sync with the development team',
    'Attend the scheduled team meeting to discuss progress, blockers, and next steps for the sprint.'
),
(
    'Code review',
    'Review pull requests from teammates',
    'Go through open pull requests, provide feedback, and approve or request changes as necessary.'
),
(
    'Update documentation',
    'Revise API documentation',
    'Update the API documentation to reflect recent changes in endpoints and data models.'
),
(
    'Deploy to staging',
    'Deploy latest build to staging environment',
    'Deploy the most recent application build to the staging server for QA testing and validation.'
);