*** Settings ***
Library  RoboBucketeer

*** Variables ***
${TARGET_DOMAIN}    infogalactic.com
${SUBLIST3R_REPORT}   /home/umar/Desktop/RobotFramework-Dev/RoboBucketeer/test/infogalactic     
${YAML_REPORT}  /home/umar/Desktop/RobotFramework-Dev/RoboBucketeer/test/infogalactic.yaml


*** Test Case ***
Run Bucketeer against the target
    enumerate subdomain     ${TARGET_DOMAIN}  ${SUBLIST3R_REPORT}   ${YAML_REPORT}