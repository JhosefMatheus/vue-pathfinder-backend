import { Requirement } from "@prisma/client";

export interface IGetRequirementsParams {
    classId: string;
    requirementGroupId: string;
}

export interface IGetRequirements {
    flag: boolean;
    message: string;
    requirements?: Requirement[]
}