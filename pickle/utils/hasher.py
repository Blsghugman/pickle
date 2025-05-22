import pickle
import hashlib


def hash_pickle(obj, protocol=pickle.HIGHEST_PROTOCOL):
    try:
        data = pickle.dumps(obj, protocol=protocol)
        return hashlib.sha256(data).hexdigest()
    except Exception as e:
        # 返回基于异常描述的伪哈希（可选）
        err_str = f"{type(e).__name__}: {e}"
        return hashlib.sha256(err_str.encode()).hexdigest()
