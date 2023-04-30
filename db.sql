-- CREATE TABLE `activities` (
--   `id` int(11) NOT NULL AUTO_INCREMENT,
--   `title` varchar(100) NOT NULL,
--   `email` varchar(100) DEFAULT NULL,
--   `created_at` datetime(6) NOT NULL,
--   `updated_at` datetime(6) NOT NULL,
--   `deleted_at` datetime(6) DEFAULT NULL,
--   PRIMARY KEY (`id`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- todo4.activities definition

CREATE TABLE `activities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- todo4.todos definition

-- CREATE TABLE `todos` (
--   `id` int(11) NOT NULL AUTO_INCREMENT,
--   `title` varchar(100) NOT NULL,
--   `priority` varchar(50) NOT NULL,
--   `is_active` tinyint(1) NOT NULL,
--   `created_at` datetime(6) NOT NULL,
--   `updated_at` datetime(6) DEFAULT NULL,
--   `deleted_at` datetime(6) DEFAULT NULL,
--   `activity_group_id_id` int(11) DEFAULT NULL,
--   PRIMARY KEY (`id`),
--   KEY `todos_activity_group_id_id_807345a4_fk_activities_id` (`activity_group_id_id`),
--   CONSTRAINT `todos_activity_group_id_id_807345a4_fk_activities_id` FOREIGN KEY (`activity_group_id_id`) REFERENCES `activities` (`id`)
-- ) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- todo4.todos definition

CREATE TABLE `todos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `activity_group_id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `is_active` tinyint(1) NOT NULL DEFAULT '1',
  `priority` enum('very-low','low','normal','high','very-high') NOT NULL DEFAULT 'very-high',
  `created_at` datetime NOT NULL,
  `updated_at` datetime DEFAULT NULL,
  `deleted_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;