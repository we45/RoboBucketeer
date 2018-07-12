import sublist3r
import dns.resolver
from termcolor import colored
import argparse
import yaml
import sys


class RoboBucketeer(object):

    def __init__(self):
        self.cname_lookups = ['cloudfront', 'amazonaws', 'zendesk', 'digitaloceanspaces']
        self.sub_results = {}

    def enum_sub_domains(self,domain,report_path):
        sublist3r.main('{0}'.format(domain), None, '{0}.txt'.format(report_path), ports=None, silent=False, verbose=True,
                        enable_bruteforce=False, engines=None)

    def write_to_yaml(self,yaml_path):
        for x in list(self.sub_results.keys()):
            if self.sub_results[x] == []:
                del self.sub_results[x]
        with open(yaml_path, 'w') as outfile:
            yaml.dump(self.sub_results, outfile, default_flow_style = False)

    def enum_cloud_subs(self, report_path, yaml_path):
        try:
            with open('{0}.txt'.format(report_path),'r') as subfile:
                for line in subfile.readlines():
                    print('Trying for: '+line)
                    self.sub_results[line.rstrip()] = []
                    answers = ''
                    try:
                        answers = dns.resolver.query(line.rstrip(), 'CNAME')
                    except Exception as e:
                        pass
                    for single in answers:
                        for cn in self.cname_lookups:
                            if cn in single.to_text():
                                print(colored("Domain: {0}, Identified CNAME with Interesting Data: {1}".format(line.rstrip(), single.to_text()), color='red'))
                                self.sub_results[line.rstrip()].append(single.to_text())
        except KeyboardInterrupt:
            self.write_to_yaml(yaml_path)
            print("Bye...")

    def enumerate_subdomain(self,domain,report_path,yaml_path):
        self.enum_sub_domains(domain,report_path)
        self.enum_cloud_subs(report_path,yaml_path)
        self.write_to_yaml(yaml_path)











