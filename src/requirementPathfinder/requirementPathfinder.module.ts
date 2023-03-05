import { Module } from "@nestjs/common";
import { RequirementPathfinderController } from "./requirementPathfinder.controller";
import { RequirementPathfinderService } from "./requirementPathfinder.service";

@Module({
    controllers: [RequirementPathfinderController],
    providers: [RequirementPathfinderService]
})
export class RequirementPathfinderModule {}