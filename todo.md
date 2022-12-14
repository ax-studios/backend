# Todo list

- [ ] create required @properties in all models
- [ ] 1. add CRUD operations
- [ ] 2. add auth
- [ ] 3. limit CRUD operations based on user role

## Done

- [x] Create resolver functions
- [x] Create additional paramerters/relations to Models
  - [x] add classes & class_teacher to "teachers"
  - [x] add class_teacher & classes to "subjects"
  - [x] add teachers to "class"
- [x] match graphql schema with resolver functions
- [x] resolve case-sensitivity issue (for name, subject names, etc)
- [x] Create trigger to avoid insertion of same student-teacher pairs (same for class_to_subject_techer table)
