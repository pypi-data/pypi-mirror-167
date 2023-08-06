import pandas as pd
from datetime import datetime


class OrderHandle:
    def __init__(self, mt5):
        self.mt5 = mt5

    def open_position(self, pair, order_type, size, op_price=0.0, tp_price=0.0, sl_price=0.0, mg_number=5240, ocm=""):
        size = float("{0:4.2f}".format(size))
        if size < 0.01:
            size = 0.01

        symbol_info = self.mt5.symbol_info(pair)
        if symbol_info is None:
            print(pair, "not found")
            return

        if not symbol_info.visible:
            print(pair, "is not visible, trying to switch on")
            if not mt5.symbol_select(pair, True):
                print("symbol_select({}}) failed, exit", pair)
                return

        order = 'BUY'
        action = self.mt5.TRADE_ACTION_DEAL
        price = 0
        sl = sl_price
        tp = tp_price
        if order_type == "BUY":
            order = self.mt5.ORDER_TYPE_BUY
            price = self.mt5.symbol_info_tick(pair).ask

        if order_type == "SELL":
            order = self.mt5.ORDER_TYPE_SELL
            price = self.mt5.symbol_info_tick(pair).bid

        if order_type == "BUYLIMIT":
            order = self.mt5.ORDER_TYPE_BUY_LIMIT
            price = op_price
            action = self.mt5.TRADE_ACTION_PENDING

        if order_type == "BUYSTOP":
            order = self.mt5.ORDER_TYPE_BUY_STOP
            price = op_price
            action = self.mt5.TRADE_ACTION_PENDING

        if order_type == "SELLLIMIT":
            order = self.mt5.ORDER_TYPE_SELL_LIMIT
            price = op_price
            action = self.mt5.TRADE_ACTION_PENDING

        if order_type == "SELLSTOP":
            order = self.mt5.ORDER_TYPE_SELL_STOP
            price = op_price
            action = self.mt5.TRADE_ACTION_PENDING

        d = self.get_symbol_info(pair, 'digits')
        if d == 3:
            sl = float('{0:5.3f}'.format(sl))
            tp = float('{0:5.3f}'.format(tp))
        elif d == 2:
            sl = float('{0:4.2f}'.format(sl))
            tp = float('{0:4.2f}'.format(tp))
        else:
            sl = float('{0:7.5f}'.format(sl))
            tp = float('{0:7.5f}'.format(tp))

        request = {
            "action": action,
            "symbol": pair,
            "volume": float(size),
            "type": order,
            "price": price,
            "sl": sl,
            "tp": tp,
            "deviation": 5,
            "magic": mg_number,
            "comment": ocm,
            "type_time": self.mt5.ORDER_TIME_GTC,
            "type_filling": self.mt5.ORDER_FILLING_IOC,
        }

        result = self.mt5.order_send(request)

        if result.retcode != self.mt5.TRADE_RETCODE_DONE:
            result_dict = result._asdict()
            print(result_dict)
            return -1   # order ticket = -1 mean order send error
        else:
            msg = "Order successfully placed...! Symbol: {0} Type: {1} Lot: {2}".format(pair, order_type, size)
            print(msg)
            result_dict = result._asdict()
            otk = result_dict['order']  # order ticket
            return otk

    def get_symbol_info(self, sym_f, sel=None):
        tm = self.mt5.symbol_info_tick(sym_f).time
        bid = self.mt5.symbol_info_tick(sym_f).bid
        ask = self.mt5.symbol_info_tick(sym_f).ask
        spread = self.mt5.symbol_info(sym_f).spread
        digits = self.mt5.symbol_info(sym_f).digits
        point = self.mt5.symbol_info(sym_f).point
        positions = self.mt5.positions_get(symbol=sym_f)
        lot = 0
        if len(positions) > 0:
            for position in positions:
                lot += position[9]
        d = {'time': tm, 'bid': bid, 'ask': ask, 'spread': spread, 'digits': digits, 'point': point, 'lot': lot}
        if sel is None:
            return d
        else:
            return d[sel]

    def modify_position(self, symbol_f, ticket, nw_sl=0.0, nw_tp=0.0):
        positions = self.mt5.positions_get(symbol=symbol_f)
        sif = self.get_symbol_info(symbol_f)
        p = sif['point']
        d = sif['digits']
        bid = sif['bid']
        div = 10 * p  # min step size
        if positions is None:
            print("Cannot read position on {0}".format(symbol_f))
            return 0
        elif len(positions) > 0:
            for position in positions:
                tk = position_data(position, 'ticket')
                order_type = position_data(position, 'ortype')
                opp = position_data(position, 'open_price')
                sl = position_data(position, 'sl')
                tp = position_data(position, 'tp')
                mg = position_data(position, 'mgNB')
                ocm = position_data(position, 'comment')

                fmt = '{0:2.0f}'
                if d == 1:
                    fmt = '{0:3.1f}'
                if d == 2:
                    fmt = '{0:4.2f}'
                if d == 3:
                    fmt = '{0:5.3f}'
                if d == 4:
                    fmt = '{0:6.4f}'
                if d == 5:
                    fmt = '{0:7.5f}'

                if nw_sl > 0:
                    nw_sl = float(fmt.format(nw_sl))
                else:
                    nw_sl = float(fmt.format(sl))

                if nw_tp > 0:
                    nw_tp = float(fmt.format(nw_tp))
                else:
                    nw_tp = float(fmt.format(tp))

                if abs(nw_sl - sl) < div and abs(nw_tp - tp) < div:
                    return

                request = {
                    'action': self.mt5.TRADE_ACTION_SLTP,
                    'position': tk,
                    'symbol': symbol_f,
                    'sl': nw_sl,
                    'tp': nw_tp,
                    'magic': mg,
                }

                if tk == ticket:
                    result = self.mt5.order_send(request)
                    if result.retcode != self.mt5.TRADE_RETCODE_DONE:
                        print(result)
                        return False
                    else:
                        if order_type == 0:
                            pfp = (nw_sl - opp) / p
                        else:
                            pfp = (opp - nw_sl) / p
                        print('Order successfully modified...! '
                              '{0} SL: {1:7.5f} Profit_Point: {2:2.0f}'.format(symbol_f, nw_sl, pfp))
                        return True

    def get_all_position(self, symbol=None):
        if symbol is None:
            res = self.mt5.positions_get()
        else:
            res = self.mt5.positions_get(symbol=symbol)

        if res is not None and res != ():
            df = pd.DataFrame(list(res), columns=res[0]._asdict().keys())
            df['time'] = pd.to_datetime(df['time'], unit='s')
            return df
        else:
            return pd.DataFrame()

    def delete_pending(self, ticket):
        close_request = {
            "action": self.mt5.TRADE_ACTION_REMOVE,
            "order": ticket,
            "type_time": self.mt5.ORDER_TIME_GTC,
            "type_filling": self.mt5.ORDER_FILLING_IOC,
        }
        result = self.mt5.order_send(close_request)

        if result.retcode != self.mt5.TRADE_RETCODE_DONE:
            result_dict = result._asdict()
            print(result_dict)
            return False
        else:
            print('Delete complete...')
            return True

    def close_position(self, deal_id, order_type, symbol, volume, pf):
        if order_type == self.mt5.ORDER_TYPE_BUY:
            order_type = self.mt5.ORDER_TYPE_SELL
            price = self.mt5.symbol_info_tick(symbol).bid
        else:
            order_type = self.mt5.ORDER_TYPE_BUY
            price = self.mt5.symbol_info_tick(symbol).ask

        close_request = {
            "action": self.mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": float(volume),
            "type": order_type,
            "position": deal_id,
            "price": price,
            "magic": 234000,
            "comment": "Close trade",
            "type_time": self.mt5.ORDER_TIME_GTC,
            "type_filling": self.mt5.ORDER_FILLING_IOC,
        }

        result = self.mt5.order_send(close_request)

        if result.retcode != self.mt5.TRADE_RETCODE_DONE:
            result_dict = result._asdict()
            print(result_dict)
            return False
        else:
            ort = "SELL"  # Use for close Buy
            if order_type == 1:
                ort = "BUY"  # Use for close Sell
            msg = "Order successfully closed...! Symbol: {0} Type: {1} Size: " \
                  "{2} Profit {3:4.2f}".format(symbol, ort, volume, pf)
            print(msg)
            return True

    def close_positions_by_symbol(self, symbol_f):
        positions = self.mt5.positions_get(symbol=symbol_f)
        if positions is None:
            print("Cannot read position on {0}".format(symbol_f))
        elif len(positions) > 0:
            for position in positions:
                pif = position_data(position)
                tk = pif['ticket']
                order_type = pif['order_type']
                lots = pif['lot']
                pf = pif['swap'] + pif['profit'] - (lots * 8)  # swap+pf+commission
                self.close_position(tk, order_type, symbol_f, lots, pf)

    def total_position_on_symbol(self, symbol_f):
        positions = self.mt5.positions_get(symbol=symbol_f)
        if positions is None:
            return 0
        else:
            ln = len(positions)
            return ln

    def total_sell_on_symbol(self, symbol_f):
        positions = self.mt5.positions_get(symbol=symbol_f)
        tt = 0
        if positions is None:
            return 0
        elif len(positions) > 0:
            for position in positions:
                order_type = position[5]
                if order_type == 1:
                    tt += 1
        return tt

    def total_buy_on_symbol(self, symbol_f):
        positions = self.mt5.positions_get(symbol=symbol_f)
        tt = 0
        if positions is None:
            return 0
        elif len(positions) > 0:
            for position in positions:
                order_type = position[5]
                if order_type == 0:
                    tt += 1
        return tt

    def total_pending_on_symbol(self, symbol_f, pending_type="BUYLIMIT"):
        p_type = 0
        if pending_type == "BUYLIMIT":
            p_type = self.mt5.ORDER_TYPE_BUY_LIMIT
        if pending_type == "BUYSTOP":
            p_type = self.mt5.ORDER_TYPE_BUY_STOP
        if pending_type == "SELLLIMIT":
            p_type = self.mt5.ORDER_TYPE_SELL_LIMIT
        if pending_type == "SELLSTOP":
            p_type = self.mt5.ORDER_TYPE_SELL_STOP

        positions = self.mt5.orders_get(symbol=symbol_f)
        tt = 0
        if positions is None:
            return 0
        elif len(positions) > 0:
            for position in positions:
                order_type = position[5]
                if order_type == p_type:
                    tt += 1
        return tt

    def get_average_spread(self, symbol_f):
        # NOTE: This is my calculate method is not true average spread
        sif = self.get_symbol_info(symbol_f)
        spread = sif['spread']
        point = sif['point']
        try:
            rates = self.mt5.copy_rates_from_pos(symbol_f, self.mt5.TIMEFRAME_H4, 0, 10)
            av = []
            for i in range(10):
                hg = rates[i][2]
                lw = rates[i][3]
                av.append(hg - lw)
            avs = sum(av) / len(av)
            sav = avs / 10
            sp_avg = sav / point
            sp_avg = int(sp_avg)
            return sp_avg
        except Exception as e:
            print(e)
            return spread

    def get_last_position_time(self, symbol_f):
        positions = self.mt5.positions_get(symbol=symbol_f)
        lst_tm = 0
        if positions is None:
            return 0
        elif len(positions) > 0:
            for position in positions:
                tm = position[1]
                if tm > lst_tm:
                    lst_tm = tm
        return lst_tm

    def get_server_time(self, sym_f, time_frame, shift=0):
        # tf = mt5.TIMEFRAME_H4
        rates = self.mt5.copy_rates_from_pos(sym_f, time_frame, 0, shift + 2)
        rates_frame = pd.DataFrame(rates)
        time_s = rates_frame['time'][shift + 1]
        rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')
        tm = rates_frame['time'][shift + 1]
        hh = tm.strftime("%H")
        mi = tm.strftime("%M")
        sc = tm.strftime("%S")
        dy = tm.strftime("%d")
        ft = tm.strftime("%Y-%m-%d %H:%M:00")
        curr_tm = {'Hour': int(hh), 'Minute': int(mi), 'Sec': sc, 'Day': int(dy), 'FullTime': ft, 'Raw': time_s}
        return curr_tm

    def get_bar_price(self, sym_f, tf, bar_pos=1):
        # tf = mt5.TIMEFRAME_H1 or M30, H4, D1
        rates = self.mt5.copy_rates_from_pos(sym_f, tf, 0, bar_pos + 2)
        rates_frame = pd.DataFrame(rates)
        hg = rates_frame['high'][1]  # bar index is [0, 1, 2, 3, 4] where 4 is current bar
        lw = rates_frame['low'][1]
        op = rates_frame['open'][1]
        cl = rates_frame['close'][1]
        res = {'Open': op, 'High': hg, 'Low': lw, 'Close': cl}
        return res


# Static function
def position_data(pos, select_data=None):
    dt = {'ticket': pos[0],
          'open_time': pos[1],
          'order_type': pos[5],  # 0=buy, 1=sell
          'ortype': pos[5],  # same as order_type
          'mgNB': pos[6],
          'lot': pos[9],
          'open_price': pos[10],
          'sl': pos[11],
          'tp': pos[12],
          'curr_price': pos[13],
          'swap': pos[14],
          'profit': pos[15],
          'symbol': pos[16],
          'comment': pos[17]
          }
    if select_data is None:
        return dt
    else:
        return dt[select_data]


def my_trade_symbol():
    # These symbols must be in MT5
    x = ["AUDUSD", "AUDCAD", "AUDCHF", "AUDJPY", "AUDNZD", "CHFJPY", "CADCHF",
         "CADJPY", "EURGBP", "EURAUD", "EURJPY", "EURCHF", "EURNZD", "EURCAD",
         "EURUSD", "GBPUSD", "GBPAUD", "GBPCHF", "GBPCAD", "GBPJPY", "GBPNZD",
         "NZDCAD", "NZDCHF", "NZDJPY", "NZDUSD", "USDCHF", "USDJPY", "USDCAD",
         "USDSGD", "XAUUSD", "BTCUSD", "ETHUSD", "LNKUSD", "ADAUSD", "DOGUSD"]
    return x


def get_local_time(select=None):
    now = datetime.now()
    hh = int(now.strftime("%H"))
    mm = int(now.strftime("%M"))
    ss = int(now.strftime("%S"))
    data = {'HH': hh, 'MM': mm, 'SS': ss}
    if select is None:
        return data
    else:
        return data[select]


def convert_time_sec_to_hour(time_sec):
    tm = pd.to_datetime(time_sec, unit='s')
    ort = {'Hour': int(tm.strftime("%H")), 'Minute': int(tm.strftime("%M")),
           'Sec': int(tm.strftime("%S")), 'Raw': time_sec}
    return ort


def connect(mt5, acc, psw, serv, pth):
    if not mt5.initialize(path=pth, login=acc, password=psw, server=serv):
        print("initialize() failed, error code =", mt5.last_error())

    authorized = mt5.login(acc, password=psw, server=serv)
    if authorized:
        print("Connected: Connecting to MT5 Client")
    else:
        print("Failed to connect at account #{}, error code: {}"
              .format(acc, mt5.last_error()))
    return mt5
