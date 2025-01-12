import json


def SBT_(cur_root_id, node_list):
    cur_root = node_list[cur_root_id]
    tmp_list = []
    tmp_list.append("(")

    str = cur_root['type']
    tmp_list.append(str)

    if 'children' in cur_root:
        chs = cur_root['children']
        for ch in chs:
            tmp_list.extend(SBT_(ch, node_list))
    tmp_list.append(")")
    tmp_list.append(str)
    return tmp_list

def SBTCODE_(cur_root_id, node_list):
    cur_root = node_list[cur_root_id]
    tmp_list = []
    tmp_list.append("(")

    str = cur_root['type']
    tmp_list.append(str)
    
    if 'value' in cur_root:
        code = cur_root['value']
        tmp_list.append(code)

    if 'children' in cur_root:
        chs = cur_root['children']
        for ch in chs:
            tmp_list.extend(SBTCODE_(ch, node_list))
    tmp_list.append(")")
    tmp_list.append(str)
    return tmp_list



def get_sbt_structure(ast_file, out_file):
    with open(ast_file, 'r') as ast_file:
        with open(out_file, 'w+') as out:
            asts = ast_file.readlines()
            for a in asts:
                a = json.loads(a)
                ast_sbt = SBT_(0, a)
                out.write(' '.join(ast_sbt) + '\n')


def get_sbtcode_structure(ast_file, out_file):
    with open(ast_file, 'r') as ast_file:
        with open(out_file, 'w+') as out:
            asts = ast_file.readlines()
            for a in asts:
                a = json.loads(a)
                ast_sbt = SBTCODE_(0, a)
                out.write(' '.join(ast_sbt) + '\n')


# get_sbt_structure("ast.json", "ast.sbt")

get_sbtcode_structure("seCNN_ast.json", "seCNN.ast")