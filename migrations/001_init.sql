CREATE TABLE IF NOT EXISTS teachers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50) NOT NULL,
  gender TEXT NOT NULL,
  photo_url TEXT UNIQUE NOT NULL,
  votes INT NOT NULL DEFAULT 0,

  CONSTRAINT chk_teachers_gender CHECK(LOWER(gender) IN ('male', 'female')),
  CONSTRAINT chk_teachers_photo_url
  CHECK(photo_url ~* '^https://www\.aiub\.edu/Files/Uploads/public-employee-profiles/profile-pictures/.[0-9]{0,9}\.jpg$'),
  CONSTRAINT chk_teachers_votes CHECK(votes >= 0)
);
