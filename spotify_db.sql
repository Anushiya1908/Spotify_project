CREATE DATABASE spotify_df;
USE spotify_df;
CREATE TABLE spotify_tracks (id INT AUTO_INCREMENT PRIMARY KEY,
Track_Name VARCHAR(225) , 
Artists VARCHAR(225) ,
Album VARCHAR(225),
Popularity VARCHAR(225),
Duration FLOAT
);
 TRUNCATE table spotify_tracks;
 SELECT * from spotify_tracks;
 
 SELECT * from spotify_tracks ORDER BY Popularity DESC 
 LIMIT 1;
 
 SELECT * from spotify_tracks WHERE Duration > 4.00;
 
 SELECT
      CASE 
	      WHEN Popularity >= 90 THEN 'Most Popular'
          WHEN Popularity >= 70 THEN 'Popular'
	      ELSE 'Less Popular'
          END AS Popularity_Range,
COUNT(*) AS Track_count
FROM spotify_tracks
GROUP BY Popularity_Range; 