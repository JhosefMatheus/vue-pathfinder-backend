import { Subrequirement } from "@prisma/client";

export interface IGetSubRequirementsParams {
    requirementId: string;
}

export interface IGetSubRequirements {
    flag: boolean;
    message: string;
    subRequirements?: Subrequirement[]
}