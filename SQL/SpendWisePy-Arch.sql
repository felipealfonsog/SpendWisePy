

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


CREATE TABLE `expenses` (
  `id` int NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `amount` decimal(10,2) NOT NULL,
  `name` varchar(255) NOT NULL,
  `date` date DEFAULT NULL
) 




ALTER TABLE `expenses`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `expenses`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;
