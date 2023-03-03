import { Module } from "@nestjs/common";
import { SubRequirementController } from "./subRequirement.controller";
import { SubRequirementService } from "./subRequirement.service";

@Module({
    controllers: [SubRequirementController],
    providers: [SubRequirementService]
})
export class SubRequirementModule {}