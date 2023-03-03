import { Module } from '@nestjs/common';
import { ConfigModule } from '@nestjs/config';
import { AuthModule } from './auth/auth.module';
import { ClassModule } from './class/class.module';
import { PathfinderModule } from './pathfinder/pathfinder.module';
import { PrismaModule } from './prisma/prisma.module';
import { RequirementModule } from './requirement/requirement.module';
import { RequirementGroupModule } from './requirementGroup/requirementGroup.module';
import { SubRequirementModule } from './subRequirement/subRequirement.module';
import { TokenModule } from './token/token.module';

@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true
    }),
    AuthModule,
    PrismaModule,
    TokenModule,
    PathfinderModule,
    ClassModule,
    RequirementGroupModule,
    RequirementModule,
    SubRequirementModule
  ]
})
export class AppModule {}
