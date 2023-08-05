import torch
import torchvision
import matplotlib.pyplot as plt
import numpy as np
random_seed = 1
torch.backends.cudnn.enabled = False
torch.manual_seed(random_seed)
from scipy.signal import savgol_filter

import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import os

import socket
import pickle, json, requests, ast

import pkg_resources


IP = '127.0.0.1:8000'

def login(username, key):
  print("Logging in...")
  credentials = {'username':username, 'key':key, 'task':'login'}
  response = requests.post('http://'+IP+'/api/python_login', data=credentials)
  if response.text == '1':
    os.environ["username"] = username
    os.environ["key"] = key
    print("Successfully connected to tunerml!")
  else:
    print("Credentials could not be verified.")


def project(project_name):
  installed_packages = pkg_resources.working_set #Save all installed packages for that project
  installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
  
  print(installed_packages_list)
  data = {'project_name': project_name, 'installed_packages': str(installed_packages_list), 'username': os.environ['username'], 'key': os.environ['key']}
  response = requests.post('http://'+IP+'/api/create_project', data=data)
  
  if response.text == '0':
    print("Authentication failed")
  else:
    response_dict = ast.literal_eval(response.text)
    print(response_dict)
    
    if response_dict['exists'] == 0:
      print("Created a new project.")
      os.environ["project_id"] = str(response_dict['project_id'])
    else:
      print("Using a project that already exists.")
      os.environ["project_id"] = str(response_dict['project_id'])


      

def block(block_name, connect_with, project_id):

  data = {'project_id': project_id, 'block_name': block_name, 'connect_with': connect_with, 'username': os.environ['username'], 'key': os.environ['key']}
  response = requests.post('http://'+IP+'/api/create_block', data=data)
  
  if response.text == '0':
    print("Authentication failed")
  else:
    response_dict = ast.literal_eval(response.text)
    print(response_dict)
    
    if response_dict['connect_with'] == 0:
      print("Couldn't find connecting block. Please create it.")
      return

    return response_dict['block_id'] 


      
  
def node(node_name, connect_with, node_description):
  
  data = {'node_name': node_name, 'connect_with': connect_with, 'node_description': node_description,
          'username': os.environ['username'], 'key': os.environ['key'], 'project_id': os.environ['project_id'],
          'start_node': int(start_node), 'end_node': int(end_node)}
  response = requests.post('http://'+IP+'/api/create_node', data=data)

  if response.text == '0':
    print("Authentication failed")
  else:
    response_dict = ast.literal_eval(response.text)
    print(response_dict)
    
    if response_dict['connect_with'] == 0:
      print("Couldn't find connecting node. Please create it.")
      return

    return response_dict['node_id'] 





def node_input(node_id, node_input):
  data = {'block_id': node_id, 'block_input': str(node_input), 'username': os.environ['username'], 'key': os.environ['key']}
  response = requests.post('http://'+IP+'/api/set_node_input', data=data)

def node_output(node_id, node_output):
  data = {'node_id': node_id, 'node_output': str(node_output), 'username': os.environ['username'], 'key': os.environ['key']}
  response = requests.post('http://'+IP+'/api/set_node_output', data=data)

def lr_range_finder(network, train_loader, name):

  #DEFINE OPTIMIZER

  start_lr = 1e-8
  momentum = 0.5
  optimizer = optim.SGD(network.parameters(), lr=start_lr, momentum=momentum)
  lr_scheduler = torch.optim.lr_scheduler.ExponentialLR(optimizer, gamma=1.017)

  #LR RANGE FINDER

  lr_1000 = []
  train_loss_1000 = []
  it = []

  print("Starting LR finder...")
  n_epochs = 80
  for epoch in range(1, n_epochs+1):
    network, it, optimizer, lr_1000, train_loss_1000, lr_scheduler = train(network, epoch, train_loader, it, optimizer, lr_1000, train_loss_1000, lr_scheduler)
    if len(it)>1000:
      break

  metrics = {'lr_1000':lr_1000, 'train_loss_1000':train_loss_1000, 'name': name, 'task':'initLR', 'username': os.environ['username'], 'key': os.environ['key']}
  response = requests.post('http://'+IP+'/api/python_lr_range_finder', data=metrics)
  print("Initial LR Found: ", response.text)


