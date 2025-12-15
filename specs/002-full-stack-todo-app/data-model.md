# Data Models for Full-Stack Web Todo Application

This document outlines the data models for the User and Task entities, as defined in the feature specification.

## User Entity

A **User** represents an authenticated system user.

### Attributes

| Attribute | Type | Description | Constraints |
|---|---|---|---|
| `id` | Integer | Unique identifier for the user. | Primary Key, Auto-incrementing |
| `email` | String | User's email address. | Unique, Not Null |
| `username` | String | User's chosen username. | Unique, Not Null |
| `hashed_password` | String | Securely hashed password. | Not Null |
| `created_at` | DateTime | Timestamp of user creation. | Not Null, Auto-generated |
| `updated_at` | DateTime | Timestamp of last user update. | Not Null, Auto-generated |

### Relationships

- A `User` has a one-to-many relationship with the `Task` entity. One user can have multiple tasks.

---

## Task Entity

The **Task** entity represents a single todo item.

### Attributes

| Attribute | Type | Description | Constraints |
|---|---|---|---|
| `id` | Integer | Unique identifier for the task. | Primary Key, Auto-incrementing |
| `title` | String | The title of the task. | Not Null |
| `description` | String | A detailed description of the task. | Nullable |
| `completed` | Boolean | The completion status of the task. | Not Null, Defaults to `false` |
| `created_at` | DateTime | Timestamp of task creation. | Not Null, Auto-generated |
| `updated_at` | DateTime | Timestamp of last task update. | Not Null, Auto-generated |
| `user_id` | Integer | Foreign key referencing the `User` who owns the task. | Not Null, Foreign Key |

### Relationships

- A `Task` has a many-to-one relationship with the `User` entity. Each task belongs to exactly one user.
