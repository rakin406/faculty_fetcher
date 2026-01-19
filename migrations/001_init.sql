CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  affiliate_id VARCHAR(255) UNIQUE,
  name VARCHAR(255),
  email VARCHAR(255) UNIQUE NOT NULL,
  role TEXT NOT NULL CHECK (role IN ('affiliate', 'admin')) DEFAULT 'affiliate',
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS contents (
  id SERIAL PRIMARY KEY,
  category TEXT NOT NULL CHECK (category IN ('training', 'videos', 'resources', 'scripts', 'designs')),
  title TEXT NOT NULL,
  description TEXT NOT NULL,
  url TEXT NOT NULL,
  thumbnail_url TEXT NOT NULL,
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS war_reports (
  id SERIAL PRIMARY KEY,
  user_id INT UNIQUE REFERENCES users(id),
  week_start_date DATE NOT NULL DEFAULT CURRENT_DATE,
  week_end_date DATE NOT NULL DEFAULT CURRENT_DATE + INTERVAL '6 days',
  subscription_sales INT NOT NULL DEFAULT 0,
  affiliate_signups INT NOT NULL DEFAULT 0,
  
  invites_sent INT NOT NULL DEFAULT 0,
  show_ups INT NOT NULL DEFAULT 0,
  follow_ups INT NOT NULL DEFAULT 0,
  replies_received INT NOT NULL DEFAULT 0,
  
  outbound_calls INT NOT NULL DEFAULT 0,
  live_conversations INT NOT NULL DEFAULT 0,
  emails_sent INT NOT NULL DEFAULT 0,
  texts_sent INT NOT NULL DEFAULT 0,
  social_posts INT NOT NULL DEFAULT 0,
  social_dms INT NOT NULL DEFAULT 0,
  in_person_contacts INT NOT NULL DEFAULT 0,
  
  small_business_convos INT NOT NULL DEFAULT 0,
  mid_business_convos INT NOT NULL DEFAULT 0,
  
  sales_points INT NOT NULL DEFAULT 0,
  recruiting_points INT NOT NULL DEFAULT 0,
  activity_points INT NOT NULL DEFAULT 0,
  business_points INT NOT NULL DEFAULT 0,
  total_war_score INT NOT NULL DEFAULT 0,
  
  created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
