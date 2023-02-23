/*
  Warnings:

  - A unique constraint covering the columns `[login]` on the table `User` will be added. If there are existing duplicate values, this will fail.

*/
-- DropIndex
DROP INDEX `User_fullName_key` ON `user`;

-- CreateTable
CREATE TABLE `Pathfinder` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `userId` INTEGER NOT NULL,
    `name` VARCHAR(191) NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- CreateIndex
CREATE UNIQUE INDEX `User_login_key` ON `User`(`login`);

-- AddForeignKey
ALTER TABLE `Pathfinder` ADD CONSTRAINT `Pathfinder_userId_fkey` FOREIGN KEY (`userId`) REFERENCES `User`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;
