def generate_resume(

    name,
    role,
    skills,
    education,
    projects
):

    resume = f"""

# {name}

## Target Role
{role}

---

## Skills
{skills}

---

## Education
{education}

---

## Projects
{projects}

---

## Summary

Motivated and passionate professional
with strong technical skills and
hands-on project experience.

"""

    return resume