import numpy as np
import pandas as pd
import time
from typing import List, Dict, Any
import random
import itertools
import pickle





class SpeedPerformance():
    def __init__(self, round_dig=3):
        self.round_dig = round_dig
        self.reset()
        
    def reset(self):
        self.df = pd.DataFrame()
        self.times = {}
        self.times_temp = {}
        self.counts = {}
        
    def _filter_key_name(self, name):
        name = name.replace(" ","_")
        return name
    
    def drop_name(self, name):
        del self.times[name]
        del self.counts[name]
        
    def start(self, name):
        name = self._filter_key_name(name)
        self.times_temp[name] = time.perf_counter()
        if name not in self.times:
            self.counts[name] = 0
            self.times[name] = 0

    def end(self, name):
        name = self._filter_key_name(name)
        assert name in self.times_temp
        dt = time.perf_counter() - self.times_temp[name]
        self.times[name] = np.round(self.times[name]+dt, self.round_dig)
        self.counts[name] = self.counts[name] + 1
        del self.times_temp[name]
    
    def get_report(self, sort=None):
        keys = list(self.times.keys())
        [self.drop_name(key) for key in keys if self.times[key]==0 and self.counts[key]==0]
        data = [[key, self.counts[key], np.round(self.times[key]/self.counts[key],self.round_dig), self.times[key]] for key in self.times]
        report = pd.DataFrame(data,columns=["name","counts","time_mean","total_time"])
        report["anteil %"] = np.round(report["total_time"] / report["total_time"].sum(),self.round_dig)
        return report
    
    def get_total_time(self) -> float:
        return np.round(self.get_report()["total_time"].sum(),self.round_dig)



def timer(func):
    """ 
    yoyo_fkt = timer(yoyo_fkt)
    res = yoyo_fkt(inputs)
    """
    def f(*args, **kwargs):
        name_of_fkt = func.__name__
        t0 = time.time()
        out = func(*args, **kwargs)
        t1 = time.time()
        dt = t1 - t0
        print("dt of '" +name_of_fkt+"' : ",round(dt,5))
        return out
    return f




class Helper():
    
    def sub_dict(dicti:dict, keys_keep_v:List[str]):
        """ reduces dict to subdict based on keys_keep_v """
        return {key: dicti[key] for key in dicti if key in keys_keep_v}
    
    def get_value_counts(x, dig_round=3):
        vc = pd.DataFrame(x, columns=["x"])["x"].value_counts()
        df = pd.DataFrame(columns=["name","counts","anteil"])
        df["name"] = list(vc.index)
        df["counts"] = vc.values
        df["anteil"] = np.round(vc.values/np.sum(vc.values),dig_round)
        return df
    
    def dict_swap_key_and_values(dicti):
        all_values = list(dicti.values())
        assert np.unique(all_values).shape[0] == len(all_values), "values sind nicht alle unique"
        dicti_swap = dict([(b, a) for a, b in dicti.items()])
        return dicti_swap

    
    def moving_average(array, periods=3):
        weights = np.ones(periods) / periods
        return np.convolve(array, weights, mode='valid')

    def sum_list(content:List[List[any]]) -> List[any]:
        content_v = []
        for cont in content: content_v.extend(cont)
        return content_v
        
    
    def swap(liste:list, index1:int, index2:int):
        temp = liste[index1]
        liste[index1] = liste[index2]
        liste[index2] = temp
        return liste
    
    def add_columns_to_df_with_dtype(df, col_name_v:list, dtype_v:list):
        for col_name, dtype in zip(col_name_v, dtype_v):
            df[col_name] = np.nan
            df = df.astype({col_name:dtype})
        return df


    def pad_sequences(seq, maxlen = 512, value = 0, padding = "post", truncating = "post", dtype = "long", verbose=False):
        """ funktioniert aktuell nur post """
        where_truncting = []
        num_seq = len(seq)
        paddes_seq = np.zeros((num_seq,maxlen)) + np.array(value)
        for idx,seq_i in enumerate(seq):
            len_seq_i = len(seq_i)
            if len_seq_i>maxlen:
                where_truncting.append([idx,len_seq_i-maxlen])
                if verbose: print("length_longer_than_maxlen: ",len_seq_i,maxlen)
                if truncating == "post": paddes_seq[idx,:]=np.array(seq_i)[:maxlen]
                elif truncating=="pre": paddes_seq[idx,:]=np.array(seq_i)[len_seq_i-maxlen:]
                else: assert False, "False truncating mode"
            elif len_seq_i<=maxlen:
                if padding == "post": paddes_seq[idx,:len_seq_i]=np.array(seq_i)
                elif padding == "pre": paddes_seq[idx,maxlen-len_seq_i:]=np.array(seq_i)
                else: assert False, "False padding mode"
        if dtype=="long": paddes_seq = np.int64(paddes_seq)
        elif dtype=="float": paddes_seq = np.float(paddes_seq)
        else: assert False, "False dtype"
        return paddes_seq
        
    def calc_rank(data, reverse:bool=False) -> list:
        """ [-1,2,99,4,-2] --> [4, 3, 1, 2, 5] """
        data = np.array(data)
        if reverse: data = data * -1
        temp = np.array(data).argsort().argsort()
        rank_v = (max(temp)+1) - temp
        rank_v = rank_v.tolist()
        return rank_v
    
    
    def change_column_order(df:object, col_name:str, index:int):
        """ 
        df: pd.DataFrame ,
        col_name: name der bestehenden column,
        index: neue position in column axis
        """
        cols = df.columns.tolist()
        cols.remove(col_name)
        cols.insert(index, col_name)
        return df[cols]

    def new_df_column_order(df:pd.DataFrame, new_columns:list):
        """ reorders the columns, and returns subset of columns of 'new_columns' """
        columns_available = list(df.columns)
        for column in new_columns: 
            if column not in columns_available: raise Exception(f"column '{column}' is missing!")
        df_new = pd.DataFrame(columns=new_columns)
        for column in new_columns:
            df_new[column] = df[column]
        return df_new
    
    def delete_values_from_array(np_array:np.array, delete_value_v:list) -> np.array:
        """ deletes all elements from delete_value_v in np_array """
        for delete_value in delete_value_v:
            np_array = np.delete(np_array, np.where(np_array == delete_value))
        return np_array    
    
    def get_all_combis(liste:List[str], dimension:int=2) -> List[List[str]]:
        """ Gibt alle Kombinationen raus: ohne zurücklegen + ohne beachtung der reihenfolge --> n (len(liste)) über k (dimensionen) aushaben  """
        return list(itertools.combinations(liste, dimension))
    
    def group_by_key(content:List[dict], groub_by_key:str) -> Dict[any,List[dict]]:
        """
        content = 
        [{"node_name":"1","level":"1"},
         {"node_name":"2","level":"2"},
         {"node_name":"3","level":"2"},
         {"node_name":"4","level":"3"}] 
        groub_by_key = "level"
        -->
        {
         "1":[{"node_name":"1","level":"1"}],
         "2":[{"node_name":"2","level":"2"}, {"node_name":"3","level":"2"}],
         "3":[{"node_name":"4","level":"3"}] 
         }
        """
        grouped_content = {}
        for item in content:
            key = item[groub_by_key]
            if key not in grouped_content: grouped_content[key] = []
            grouped_content[key].append(item)
        return grouped_content
            
    def chunks(lst:list, chunk_size:int, skip_last:bool=False):
        """ 
        chunk_size-sized chunks from lst. 
        skip_last:bool --> skipps the last chunk if it has less then chunk_size elements 
        """
        chunksi = [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]
        if not skip_last: return chunksi
        if len(chunksi[-1])!=chunk_size: del chunksi[-1]
        return chunksi    
    
    def sort_list_of_objects_by(content:List[dict], by_key:str, reverse:bool = True, example_for_type_not_sortable:any=None, discard_not_sortable:bool=False, append_not_sortable_at_end:bool=True) -> List[dict]:
        """  """
        temp = [i.strip() for i in by_key.split(",")]
        assert len(temp) in [1,2]
        if len(temp)==1: 
            by_key_1 = temp[0]
        else:
            by_key_1, by_key_2 = temp[0], temp[1]

        obj_level = len(temp)
            
        content_sortable, content_not_sortable = [], []
        type_not_sortable = type(example_for_type_not_sortable)
        for cont in content:
            value = None
            if cont[by_key_1] is not None:
                value = cont[by_key_1] if obj_level==1 else cont[by_key_1][by_key_2]
            if type(value) == type_not_sortable:
                content_not_sortable.append(cont)
            else:
                content_sortable.append(cont)
        content_sortable = sorted(content_sortable, key=lambda k: k[by_key_1] if obj_level==1 else k[by_key_1][by_key_2], reverse=reverse)
        content_not_sortable = ([] if discard_not_sortable else content_not_sortable)
        content_sorted = (content_sortable + content_not_sortable) if append_not_sortable_at_end else (content_not_sortable + content_sortable)
        return content_sorted
    
    def random_choice(list_of_something:List[Any]) -> List[Any]:
        """ selects very efficient a item of a list """
        t = list_of_something[random.randint(0, len(list_of_something)-1)]
        return t

    def split_into_groups_where_true(values:List[Any], where:List[bool]) -> List[List[Any]]:   
        """ 
        values=[5,3,1,6,65,1], 
        where=[0,1,1,0,1,0] 
        --> [[3, 1], [65]] 
        """
        where, values = np.array(where), np.array(values)
        assert len(where) == len(values), "müssen gleich lang sein"
        indices = np.nonzero(where[1:] != where[:-1])[0] + 1
        groups = np.split(values, indices)
        groups = groups[0::2] if where[0] else groups[1::2]
        return groups
        
        



def read_excel(path_to_file:str) -> pd.DataFrame:
    """ reads excel file, all as string """
    column_list = []
    df_column = pd.read_excel(path_to_file).columns
    for i in df_column:
        column_list.append(i)
    converter = {col: str for col in column_list} 
    df_actual = pd.read_excel(path_to_file, converters=converter)
    return df_actual


            
class Pickle:
    """ saves and loads obj like torch.save, torch.load """
    def load(path_to_file:str) -> object:
        with open(path_to_file, 'rb') as handle:
            b = pickle.load(handle)
        return b

    def save(obj:object, path_to_file:str) -> None:
        with open(path_to_file, 'wb') as handle:
            pickle.dump(obj, handle)






















