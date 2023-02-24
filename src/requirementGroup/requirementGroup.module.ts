import { Module } from "@nestjs/common";
import { RequirementGroupController } from "./requirementGroup.controller";
import { RequirementGroupService } from "./requirementGroup.service";

@Module({
    controllers: [RequirementGroupController],
    providers: [RequirementGroupService]
})
export class RequirementGroupModule {}