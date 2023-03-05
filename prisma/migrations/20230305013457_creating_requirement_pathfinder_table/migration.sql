-- CreateTable
CREATE TABLE `RequirementPathfinder` (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `requirementId` INTEGER NOT NULL,
    `pathfinderId` INTEGER NOT NULL,

    PRIMARY KEY (`id`)
) DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- AddForeignKey
ALTER TABLE `RequirementPathfinder` ADD CONSTRAINT `RequirementPathfinder_requirementId_fkey` FOREIGN KEY (`requirementId`) REFERENCES `Requirement`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE `RequirementPathfinder` ADD CONSTRAINT `RequirementPathfinder_pathfinderId_fkey` FOREIGN KEY (`pathfinderId`) REFERENCES `Pathfinder`(`id`) ON DELETE RESTRICT ON UPDATE CASCADE;
