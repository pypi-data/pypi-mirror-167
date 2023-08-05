import numpy as np
import os
import struct
import random

__all__ = ["event", "loadaerdat", "fromArray", "load"]



class event:
    def __init__(self, p, x, y, t) -> None:
        assert len(x) == len(y) and len(x) == len(p) and len(x) == len(t), "pxyt must be the same length."
        self.length = len(x)
        self.p, self.x, self.y, self.t = np.array(p), np.array(x), np.array(y), np.array(t)
    
    def keys(self):
        return ['p', 'x', 'y', 't']

    def __len__(self):
        '''
        return the len of the event
        '''
        return self.length
    
    def __getitem__(self, key):
        if isinstance(key, str):
            if key is 'p':
                return self.p
            elif key is 'x':
                return self.x
            elif key is 'y':
                return self.y
            elif key is 't':
                return self.t
            else:
                print(f"you can just extract p, x, y, t. but get {key}")
        elif isinstance(key, int):
            if key>=0 and key < self.len():
                return (self.p[key], self.x[key], self.y[key], self.t[key])
            else:
                raise IndexError("index out of range.")
        raise ValueError("unsupport extract.")
    
    def __iter__(self):
        '''
        iter the events and return a generator, event will be (p, x, y, t)
        '''
        for i in range(self.len()):
            yield (self.p[i], self.x[i], self.y[i], self.t[i])

    def __eq__(self, __o: object) -> bool:
        '''
        compare if two event are the same. 
        return True if they are same, otherwise False.
        '''
        assert isinstance(__o, event), 'event only can be compared with event.'
        return (self.x == __o.x).all() and (self.y == __o.y).all() and \
                (self.p == __o.p).all() and (self.t == __o.p).all()
    
    def len(self):
        return self.__len__()
    
    def size(self):
        return self.len()*4

    def shape(self):
        return (self.len(), 4)

    def checkValid(self, dim_p:int=-1, dim_x:int=-1, dim_y:int=-1, dim_t:int=-1):
        return len(self.getValidIndex(dim_p, dim_x, dim_y, dim_t)) == self.len()
        
    def getValidIndex(self, dim_p:int=-1, dim_x:int=-1, dim_y:int=-1, dim_t:int=-1):
        '''
        get the index  where pxyt >=0 and < dim
        '''
        index_p = (self.p >= 0)
        if dim_p > 0:
            index_p &= (self.p < dim_p)

        index_x = (self.x >= 0)
        if dim_x > 0:
            index_x &= (self.x < dim_x)

        index_y = (self.y >= 0)
        if dim_y > 0:
            index_y &= (self.y < dim_y)

        index_t = (self.t >= 0)
        if dim_t > 0:
            index_t &= (self.t < dim_t)
        valid = np.argwhere( index_p & index_x & index_y & index_t)
        return valid.reshape(-1)
    
    def _removeInvalid(self, dim_p:int=-1, dim_x:int=-1, dim_y:int=-1, dim_t:int=-1)->None:
        '''
        in-place method, keep the valid index. (0<=pxyt<dim)
        '''
        valid = self.getValidIndex(dim_p, dim_x, dim_y, dim_t)
        self.p = self.p[valid]
        self.x = self.x[valid]
        self.y = self.y[valid]
        self.t = self.t[valid]

    def removeInvalid(self, dim_p:int=-1, dim_x:int=-1, dim_y:int=-1, dim_t:int=-1):
        '''
        remove the invalid index. (0<=pxyt<dim)
        it will not change the event, but return a required event.
        '''
        valid = self.getValidIndex(dim_p, dim_x, dim_y, dim_t)
        return event(self.p[valid], self.x[valid], self.y[valid], self.t[valid])

    def _toMillisecond(self)->None:
        '''
        it will turn event's timestamp from us to ms. 
        in-place modify and will not return anything.
        '''
        self.t /= 1000
    
    def toMillisecond(self):
        '''
        turn event's timestamp from us to ms. 
        it will not change the event, but return a required event.
        '''
        return event(self.p, self.x, self.y, self.t/1000)
    
    def toArray(self, order:str="pxyt"):
        assert len(order) == 4 and order[0] in self.keys() and order[1] in self.keys() \
            and order[2] in self.keys() and order[3] in self.keys(), "order is a string consist of p, x, y, t with length 4."
        return np.column_stack((self[order[0]], self[order[1]], self[order[2]], self[order[3]]))

    def toTimeStep(self, dim:tuple, way:str="count", reshape=False)->np.ndarray:
        """
        convert events to C H W T. which mean handle events with oclock driven.
        And aggregates events at the same time interval into a step frame.
        @param:dim. the output shape of ndarray, which is a tuple with length 4.
        @param:way. how the timestamps aggregates to step.
        @param:reshape. if the Width and Height in dim are smaller than events' resolution.
        """
        if reshape:
            self._removeInvalid(dim_p=dim[0], dim_x=dim[2], dim_y=dim[1])
        t = (dim[3]*(self.t / (max(self.t)+1))).astype(int)
        if way == "count":
            steps = np.zeros(dim).reshape(-1)
            index = np.ravel_multi_index((self.p, self.y, self.x, t), dim)
            weight_index = np.bincount(index)
            steps[:weight_index.size] = weight_index
            steps = steps.reshape(dim)
            return steps
    
    def domainReverse(self, domain, HW, filter_events):
        '''
        reverse specific events(filter_events) in the whole domain.
        of course you can reverse specific events in specific domain, but I don't find if it is meaningful now. so i havn't implement it now.
        '''
        # assert domain in self.keys(), f"you can just extract p, x, y, t. but get {domain}."
        
        if domain is 'p':
            self.p[filter_events] = 1-self.p[filter_events]
        elif domain is 'x':
            self.x[filter_events] = HW[1]-1-self.x[filter_events]
        elif domain is 'y':
            self.y[filter_events] = HW[0]-1-self.y[filter_events]
        elif domain is 't': 
            self.t[filter_events] = max(self.t) -self.t[filter_events]  
        
    def domainDrift(self, domain, HW, filter_events, distance, recurrent=False):
        '''
        drift specific events range[begin, end) in the whole domain.
        of course you can drift specific events in specific domain, but I don't find if it is meaningful now. so i havn't implement it now.
        '''
        # assert domain in self.keys(), f"you can just extract p, x, y, t. but get {domain}."
        
        if domain is 'p':
            distance = np.random.randint(-int(distance*2), int(distance*2)+1) 
            self.p[filter_events] = self.p[filter_events] + distance
            if recurrent:
                self.p[filter_events] %= 2
            else:
                self._removeInvalid(dim_p=2)
        elif domain is 'x':
            distance = np.random.randint(-int(distance*HW[1]), int(distance*HW[1])+1) 
            self.x[filter_events] = self.x[filter_events] + distance
            if recurrent:
                self.x[filter_events] %= HW[1]
            else:
                self._removeInvalid(dim_x=HW[1])
        elif domain is 'y':
            distance = np.random.randint(-int(distance*HW[0]), int(distance*HW[0])+1) 
            self.y[filter_events] = self.y[filter_events] + distance
            if recurrent:
                self.y[filter_events] %= HW[0]
            else:
                self._removeInvalid(dim_y=HW[0])
        elif domain is 't':
            resolution = max(self.t)+1
            distance = np.random.randint(-int(distance*resolution), int(distance*resolution)+1) 
            self.t[filter_events] = self.t[filter_events] + distance
            if recurrent:
                self.t[filter_events] %= resolution
            else:
                self._removeInvalid(dim_t=resolution)  

    def event_drop(self, HW):
        x = self.x
        y = self.y
        t = self.t
        p = self.p
        option = np.random.randint(0, 4) # 0: identity, 1: drop_by_time, 2: drop_by_area, 3: random_drop
        if option == 1: # drop_by_time
            T = np.random.randint(1, 10)/10.0 #np.random.uniform(0.1, 0.9)
            self.drop_by_time(T=T)
        elif option == 2: # drop by area
            area_ratio = np.random.randint(1, 6) / 20.0 #np.random.uniform(0.05, 0.1, 0.15, 0.2, 0.25)
            self.drop_by_area(resolution=HW, area_ratio=area_ratio)
        elif option == 3: # random drop
            ratio = np.random.randint(1, 10)/10.0 #np.random.uniform(0.1, 0.9)
            self.random_drop(ratio=ratio)

        if len(self.x) == 0:  # avoid dropping all the events
            self.p = p
            self.x = x
            self.y = y
            self.t = t

    def drop_by_time(self,T= 0):
        # assert 0.1 <= T <= 0.5

        # time interval
        t_start = np.random.uniform(0, 1)
        if T == 0: # randomly choose a value between [0.1, 0.9]
            T = np.random.randint(1, 10)/10.0
        t_end = t_start + T

        timestamps = self.t
        max_t = max(timestamps) 
        idx = (timestamps < (max_t*t_start)) | (timestamps > (max_t*t_end)) # remaining events that are not within the given time interval

        self.p = self.p[idx]
        self.x = self.x[idx]
        self.y = self.y[idx]
        self.t = self.t[idx]

    def drop_by_area(self,resolution, area_ratio=0):
        # assert 0.1 <= area_ratio <= 0.3 

        # get the area whose events are to be dropped
        x0 = np.random.uniform(resolution[0])
        y0 = np.random.uniform(resolution[1])

        if area_ratio == 0:
            area_ratio = np.random.randint(1, 6)/20.0

        x_out = resolution[0] * area_ratio
        y_out = resolution[1] * area_ratio

        x0 = int(max(0, x0 - x_out/2.0))
        y0 = int(max(0, y0 - y_out/2.0))

        x1 = min(resolution[0], x0 + x_out)
        y1 = min(resolution[1], y0 + y_out)

        xy = (x0, x1, y0, y1) # rectangele to be dropped

        idx1 = (self.x < xy[0]) | (self.x > xy[1])
        idx2 = (self.y < xy[2]) | (self.y > xy[3])
        idx = idx1 & idx2

        self.p = self.p[idx]
        self.x = self.x[idx]
        self.y = self.y[idx]
        self.t = self.t[idx]

    def random_drop(self,ratio = 0):
        # assert 0.1 <= ratio <= 0.5

        if ratio == 0:
            ratio = np.random.randint(1, 10)/10.0

        N = len(self.x) # number of total events
        num_drop = int(N * ratio) # number of events to be dropped
        idx = random.sample(list(np.arange(0, N)), N-num_drop)

        self.p = self.p[idx]
        self.x = self.x[idx]
        self.y = self.y[idx]
        self.t = self.t[idx]


    def save(self, path, extention):
        """
        save event to Files with the suffix "extention".
        """
        assert extention in [".npy", ".mat", "npy", "mat"], f"event only support to save to numpy or matlab files, get extention:{extention}"
        if extention in ['.npy', 'npy']:
            np.save(path, self.toArray())
        else:
            from scipy.io import savemat
            savemat(path, {'item':self.toArray()}) # if ndarray cannot be save to mat, use tolist()

    def saveaerdat(self, path):
        """
        save to event_format. not implement till now.
        """
        raise NotImplementedError

def fromArray(data:np.ndarray)->event:
    assert data.shape[1] == 4, "data must be a ndarray with shape (..., 4)."
    return event(data[:,0], data[:,1], data[:,2], data[:,3])  

def save(file:str, obj:event, extention:str):
    obj.save(file, extention)

def load(filename, extention)->event:
    """
    load event from Files with the suffix "extention".
    """
    assert extention in [".npy", ".mat", "npy", "mat"], f"event only support to load from numpy or matlab files, get extention:{extention}"
    if extention in ['.npy', 'npy']:
        data = np.load(filename, allow_pickle=True)
    else:
        import scipy.io as scio
        data = scio.loadmat(filename, verify_compressed_data_integrity=False)['item'].astype(np.int64)
    return fromArray(data)

def loadaerdat(filename='/tmp/aerout.dat', camera='DVS128')->event:
    """    
    This function read events .
    load AER data file and parse these properties of AE events:
    - timestamps (in us), 
    - x,y-position [0..127]
    - polarity (0/1)
    @param filename - path to the file to read
    @param length - how many bytes(B) should be read; default 0=whole file
    @param version - which file format version is used: "aedat" = v2, "dat" = v1 (old)
    @param debug - 0 = silent, 1 (default) = print summary, >=2 = print all debug
    @param camera='DVS128' or 'DAVIS240'
    @return (ts, xpos, ypos, pol) 4-tuple of lists containing data of all events;
    """


    # camera
    if(camera == 'DVS128'):
        xmask = 0x00fe
        xshift = 1
        ymask = 0x7f00
        yshift = 8
        pmask = 0x1
        pshift = 0
        aeLen = 8
        readMode = '>II'

    elif(camera == 'DAVIS240'):
        xmask = 0x003ff000
        xshift = 12
        ymask = 0x7fc00000
        yshift = 22
        pmask = 0x800
        pshift = 11
        eventtypeshift = 31

    elif(camera == 'N'):
        xmask = 0x3fff
        xshift = 0
        ymask = 0xfffc000
        yshift = 14
        pmask = 0x10000000
        pshift = 28
        aeLen = 8 #useless
        readMode = [('t', 'u4'), ('_', 'i4')]
    elif(camera == 'N101'):
        f = open(filename, 'rb')
        raw_data = np.fromfile(f, dtype=np.uint8)
        f.close()
        raw_data = np.uint32(raw_data)
        xaddr = raw_data[0::5]
        yaddr = raw_data[1::5]
        pol = (raw_data[2::5] & 128) >> 7 #bit 7
        timestamps = ((raw_data[2::5] & 127) << 16) | (raw_data[3::5] << 8) | (raw_data[4::5])
        return event(pol, xaddr, yaddr, timestamps)
    else:
        raise ValueError("Unsupported camera: %s" % (camera))

    # find header
    aerdatafh = open(filename, 'rb')
    k = 0  # line number
    p = 0  # pointer, position on bytes
    statinfo = os.stat(filename)
    if camera == 'N':
        # This code comes from NCARS Datasets.
        lt = aerdatafh.readline()
        while lt and lt.decode("latin-1")[:2] == '% ':
            p += len(lt)
            k += 1
            lt = aerdatafh.readline()
        ev_type = np.frombuffer(aerdatafh.read(1), dtype=np.uint8)[0]
        p += 1
        ev_size = np.frombuffer(aerdatafh.read(1), dtype=np.uint8)[0]
        p += 1

    elif camera == 'DVS128':
        lt = aerdatafh.readline()
        while lt and chr(lt[0]) == "#":
            p += len(lt)
            k += 1
            lt = aerdatafh.readline()


    # conversion
    aerdatafh.seek(p)
    if camera == 'N':
        dat = np.fromfile(aerdatafh, dtype=readMode, count=-1)
        if ('_', 'i4') in readMode:
            timestamps = dat["t"].tolist()
            xaddr = np.bitwise_and(dat["_"], xmask).tolist()
            yaddr = np.right_shift(np.bitwise_and(dat["_"], ymask), yshift).tolist()
            pol = np.right_shift(np.bitwise_and(dat["_"], pmask), pshift).tolist()
            
    elif camera == 'DVS128':
        length = statinfo.st_size
        timestamps = []
        xaddr = []
        yaddr = []
        pol = []
        while p < length:
            # read data-part of file
            aerdatafh.seek(p)
            s = aerdatafh.read(aeLen)
            p += aeLen
            addr, ts = struct.unpack(readMode, s)
            x_addr = (addr & xmask) >> xshift
            y_addr = (addr & ymask) >> yshift
            a_pol = (addr & pmask) >> pshift

            timestamps.append(ts)
            xaddr.append(x_addr)
            yaddr.append(y_addr)
            pol.append(a_pol)

    return event(pol, xaddr, yaddr, timestamps)
