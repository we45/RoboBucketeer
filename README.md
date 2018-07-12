# RoboBucketeer

Robot Framework Library for RoboBuckteer -  S3 Buckets &amp; Subdomain Enumeration

**Supports Python 2 & Python 3**

### Install Instructions
- Clone repo with modified Sublist3r: [here](https://github.com/abhaybhargav/Sublist3r)
- Install with command: `python setup.py install`
- Create a `.robot` file that includes the keywords used by RoboBucketeer Library


### Keywords

`enumerate subdomain`  

`| enumerate subdomain  | target domain | subli3tr report  | yaml report |`

* target domain:  Domain for which subdomain need to be enumerated
* subli3tr report : where your subli3tr '.txt' results will be stored.
* yaml report: where your cloud subdomain enumeration i.e `S3 Buckets` results will be stored 

**Note:**

- Report path should be an absolute path
- Check the `RoboBucketeer.robot` inside the test directory for sample robot script