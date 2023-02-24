import { Controller, UseGuards, Get, Res } from "@nestjs/common";
import { AuthGuard } from "@nestjs/passport";
import { Response } from "express";
import { RequirementGroupService } from "./requirementGroup.service";

@UseGuards(AuthGuard("jwt"))
@Controller("requirementGroup")
export class RequirementGroupController {
    constructor(private readonly requirementGroupService: RequirementGroupService) {}

    @Get("requirementGroups")
    async getRequirementGroups(@Res() response: Response): Promise<Response> {
        const { requirementGroups } = await this.requirementGroupService.getRequirementGroups();

        return response.status(200).json({
            requirementGroups
        });
    }
}