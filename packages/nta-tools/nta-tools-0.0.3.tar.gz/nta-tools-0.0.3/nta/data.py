

from enum import Enum

# 定义枚举
class FeatureType(Enum):
    Payload_L7 = 'payload7' # Raw Payloads (application layer data only)
    Payload_L4 = 'payload4' # Raw Payloads (with transport layer packet headers)
    DPLS = 'dpls' # Directed Packet Length Sequence，带方向的包长度序列
    UPLS = 'upls' # Undirected Packet Length Sequence，无方向的包长度序列
    SPLS = 'spls' # Single-way Packet Length Sequence，单向包长度序列（大于0）
    PDS = 'pds' # Packet Direction Sequence，包方向序列（正负 1）


    # 模拟丢包现象的特征
    DPLSwPL10 = 'dplswpl10' # Directed Packet Length Sequence with 10% packet loss
    DPLSwPL20 = 'dplswpl20' # Directed Packet Length Sequence with 20% packet loss
    DPLSwPL30 = 'dplswpl30' # Directed Packet Length Sequence with 30% packet loss
    DPLSwPL40 = 'dplswpl40' # Directed Packet Length Sequence with 40% packet loss
    DPLSwPL50 = 'dplswpl50' # Directed Packet Length Sequence with 50% packet loss
    DPLSwPL60 = 'dplswpl60' # Directed Packet Length Sequence with 60% packet loss
    DPLSwPL70 = 'dplswpl70' # Directed Packet Length Sequence with 70% packet loss
    DPLSwPL80 = 'dplswpl80' # Directed Packet Length Sequence with 80% packet loss
    DPLSwPL90 = 'dplswpl90' # Directed Packet Length Sequence with 90% packet loss

    SPLSwPL10 = 'splswpl10' # Single-way Packet Length Sequence with 10% packet loss
    SPLSwPL20 = 'splswpl20' # Single-way Packet Length Sequence with 20% packet loss
    SPLSwPL30 = 'splswpl30' # Single-way Packet Length Sequence with 30% packet loss
    SPLSwPL40 = 'splswpl40' # Single-way Packet Length Sequence with 40% packet loss
    SPLSwPL50 = 'splswpl50' # Single-way Packet Length Sequence with 50% packet loss
    SPLSwPL60 = 'splswpl60' # Single-way Packet Length Sequence with 60% packet loss
    SPLSwPL70 = 'splswpl70' # Single-way Packet Length Sequence with 70% packet loss
    SPLSwPL80 = 'splswpl80' # Single-way Packet Length Sequence with 80% packet loss
    SPLSwPL90 = 'splswpl90' # Single-way Packet Length Sequence with 90% packet loss

    UPLSwPL10 = 'uplswpl10' # Undirected Packet Length Sequence with 10% packet loss
    UPLSwPL20 = 'uplswpl20' # Undirected Packet Length Sequence with 20% packet loss
    UPLSwPL30 = 'uplswpl30' # Undirected Packet Length Sequence with 30% packet loss
    UPLSwPL40 = 'uplswpl40' # Undirected Packet Length Sequence with 40% packet loss
    UPLSwPL50 = 'uplswpl50' # Undirected Packet Length Sequence with 50% packet loss
    UPLSwPL60 = 'uplswpl60' # Undirected Packet Length Sequence with 60% packet loss
    UPLSwPL70 = 'uplswpl70' # Undirected Packet Length Sequence with 70% packet loss
    UPLSwPL80 = 'uplswpl80' # Undirected Packet Length Sequence with 80% packet loss
    UPLSwPL90 = 'uplswpl90' # Undirected Packet Length Sequence with 90% packet loss

    PDSwPL10 = 'pdswpl10' # Packet Direction Sequence with 10% packet loss
    PDSwPL20 = 'pdswpl20' # Packet Direction Sequence with 20% packet loss
    PDSwPL30 = 'pdswpl30' # Packet Direction Sequence with 30% packet loss
    PDSwPL40 = 'pdswpl40' # Packet Direction Sequence with 40% packet loss

def get_all_feature_type():
    return [ft.value for ft in FeatureType]