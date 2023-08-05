from alpaca.common.models import ValidateBaseModel as BaseModel
from uuid import UUID
from datetime import datetime, date
from typing import Any, Optional, List, Union
from alpaca.trading.enums import (
    AssetClass,
    AssetStatus,
    AssetExchange,
    OrderStatus,
    OrderType,
    OrderClass,
    TimeInForce,
    OrderSide,
    PositionSide,
    AccountStatus,
    TradeActivityType,
    NonTradeActivityStatus,
    ActivityType,
    CorporateActionType,
    CorporateActionSubType,
    TradeEvent,
)
from pydantic import Field


class Asset(BaseModel):
    """
    Represents a security. Some Assets are not tradable with Alpaca. These Assets are
    marked with the flag `tradable=false`.

    For more info, visit https://alpaca.markets/docs/api-references/trading-api/assets/

    Attributes:
        id (UUID): Unique id of asset
        asset_class (AssetClass): The name of the asset class.
        exchange (AssetExchange): Which exchange this asset is available through.
        symbol (str): The symbol identifier of the asset.
        name (Optional[str]): The name of the asset.
        status (AssetStatus): The active status of the asset.
        tradable (bool): Whether the asset can be traded.
        marginable (bool): Whether the asset can be traded on margin.
        shortable (bool): Whether the asset can be shorted.
        easy_to_borrow (bool): When shorting, whether the asset is easy to borrow
        fractionable (bool): Whether fractional shares are available
    """

    id: UUID
    asset_class: AssetClass = Field(
        alias="class"
    )  # using a pydantic alias to allow parsing data with the `class` keyword field
    exchange: AssetExchange
    symbol: str
    name: Optional[str] = None
    status: AssetStatus
    tradable: bool
    marginable: bool
    shortable: bool
    easy_to_borrow: bool
    fractionable: bool


class Position(BaseModel):
    """
    Represents an open long or short holding in an asset.

    Attributes:
        asset_id (UUID): ID of the asset.
        symbol (str): Symbol of the asset.
        exchange (AssetExchange): Exchange name of the asset.
        asset_class (AssetClass): Name of the asset's asset class.
        avg_entry_price (str): The average entry price of the position.
        qty (str): The number of shares of the position.
        side (PositionSide): "long" or "short" representing the side of the position.
        market_value (str): Total dollar amount of the position.
        cost_basis (str): Total cost basis in dollars.
        unrealized_pl (str): Unrealized profit/loss in dollars.
        unrealized_plpc (str): Unrealized profit/loss percent.
        unrealized_intraday_pl (str): Unrealized profit/loss in dollars for the day.
        unrealized_intraday_plpc (str): Unrealized profit/loss percent for the day.
        current_price (str): Current asset price per share.
        lastday_price (str): Last day’s asset price per share based on the closing value of the last trading day.
        change_today (str): Percent change from last day's price.
    """

    asset_id: UUID
    symbol: str
    exchange: AssetExchange
    asset_class: AssetClass
    avg_entry_price: str
    qty: str
    side: PositionSide
    market_value: str
    cost_basis: str
    unrealized_pl: str
    unrealized_plpc: str
    unrealized_intraday_pl: str
    unrealized_intraday_plpc: str
    current_price: str
    lastday_price: str
    change_today: str


class Order(BaseModel):
    """
    Represents a request for the sale or purchase of an asset.

    Attributes:
        id (UUID): order ID generated by Alpaca.
        client_order_id (str): Client unique order ID
        created_at (datetime): Timestamp when the order was created.
        updated_at (datetime): Timestamp when the order was last updated.
        submitted_at (datetime): Timestamp when the order was submitted.
        filled_at (Optional[datetime]): Timestamp when the order was filled.
        expired_at (Optional[datetime]): Timestamp when the order expired at.
        canceled_at (Optional[datetime]): Timestamp when the order was canceled.
        failed_at (Optional[datetime]): Timestamp when the order failed at.
        replaced_at (Optional[datetime]): Timestamp when the order was replaced by a new order.
        replaced_by (Optional[UUID]): ID of order that replaces this order.
        replaces (Optional[UUID]): ID of order which this order replaces.
        asset_id (UUID): ID of the asset.
        symbol (str): Symbol of the asset.
        asset_class (AssetClass): Asset class of the asset.
        notional (Optional[str]): Ordered notional amount. If entered, qty will be null. Can take up to 9 decimal
          points.
        qty (Optional[str]): Ordered quantity. If entered, notional will be null. Can take up to 9 decimal points.
        filled_qty (Optional[str]): Filled quantity.
        filled_avg_price (Optional[str]): Filled average price. Can be 0 until order is processed in case order is
          passed outside of market hours.
        order_class (OrderClass): Valid values: simple, bracket, oco or oto.
        order_type (OrderType): Deprecated with just type field below.
        type (OrderType): Valid values: market, limit, stop, stop_limit, trailing_stop.
        side (OrderSide): Valid values: buy and sell.
        time_in_force (TimeInForce): Length of time the order is in force.
        limit_price (Optional[str]): Limit price of the order.
        stop_price (Optional[str]): Stop price of the order.
        status (OrderStatus): The status of the order.
        extended_hours (bool): If true, eligible for execution outside regular trading hours.
        legs (Optional[List[alpaca.trading.models.Order]]): When querying non-simple order_class orders in a nested style,
          an array of order entities associated with this order. Otherwise, null.
        trail_percent (Optional[str]): The percent value away from the high water mark for trailing stop orders.
        trail_price (Optional[str]): The dollar value away from the high water mark for trailing stop orders.
        hwm (Optional[str]): The highest (lowest) market price seen since the trailing stop order was submitted.
    """

    id: UUID
    client_order_id: str
    created_at: datetime
    updated_at: datetime
    submitted_at: datetime
    filled_at: Optional[datetime]
    expired_at: Optional[datetime]
    canceled_at: Optional[datetime]
    failed_at: Optional[datetime]
    replaced_at: Optional[datetime]
    replaced_by: Optional[UUID]
    replaces: Optional[UUID]
    asset_id: UUID
    symbol: str
    asset_class: AssetClass
    notional: Optional[str]
    qty: Optional[str]
    filled_qty: Optional[str]
    filled_avg_price: Optional[str]
    order_class: OrderClass
    order_type: OrderType
    type: OrderType
    side: OrderSide
    time_in_force: TimeInForce
    limit_price: Optional[str]
    stop_price: Optional[str]
    status: OrderStatus
    extended_hours: bool
    legs: Optional[List["Order"]]
    trail_percent: Optional[str]
    trail_price: Optional[str]
    hwm: Optional[str]

    def __init__(self, **data: Any) -> None:
        if "order_class" not in data or data["order_class"] == "":
            data["order_class"] = OrderClass.SIMPLE

        super().__init__(**data)


class FailedClosePositionDetails(BaseModel):
    """API response for failed close position request.

    Attributes:
        available (float): The qty available.
        code (int): The status code.
        existing_qty (float): The total qty in account.
        held_for_orders (float): The qty locked up in existing orders.
        message (str): Message for failed request.
        symbol (str): The symbol for the request.
    """

    available: float
    code: int
    existing_qty: float
    held_for_orders: float
    message: str
    symbol: str


class ClosePositionResponse(BaseModel):
    """API response for a close position request.
    Attributes:
        order_id (Optional[UUID]): ID of order that was created to liquidate the position.
        status (Optional[int]): Status code corresponding to the request to liquidate the position.
        symbol (Optional[str]): The symbol of the position being closed.
        body (Optional[dict]): Information relating to the successful or unsuccessful closing of the position.
    """

    order_id: Optional[UUID]
    status: Optional[int]
    symbol: Optional[str]
    body: Union[FailedClosePositionDetails, Order]


class PortfolioHistory(BaseModel):
    """
    Contains information about the value of a portfolio over time.

    Attributes:
        timestamp (List[int]): Time of each data element, left-labeled (the beginning of time window).
        equity (List[float]): Equity value of the account in dollar amount as of the end of each time window.
        profit_loss (List[float]): Profit/loss in dollar from the base value.
        profit_loss_pct (List[float]): Profit/loss in percentage from the base value.
        base_value (float): Basis in dollar of the profit loss calculation.
        timeframe (str): Time window size of each data element.
    """

    timestamp: List[int]
    equity: List[float]
    profit_loss: List[float]
    profit_loss_pct: List[float]
    base_value: float
    timeframe: str


class Watchlist(BaseModel):
    """
    A watchlist is an ordered list of assets. An account can have multiple watchlists.
    Learn more about watchlists in the documentation. https://alpaca.markets/docs/api-references/trading-api/watchlist/

    Attributes:
        account_id (UUID): The uuid identifying the account the watchlist belongs to
        id (UUID): The unique identifier for the watchlist
        name (str): An arbitrary string up to 64 characters identifying the watchlist
        created_at (datetime): When the watchlist was created
        updated_at (datetime): When the watchlist was last updated
        assets (Optional[List[Asset]]): The assets in the watchlist, not returned from all endpoints
    """

    account_id: UUID
    id: UUID
    name: str
    created_at: datetime
    updated_at: datetime
    assets: Optional[List[Asset]]


class Clock(BaseModel):
    """
    The market clock for US equity markets. Timestamps are in eastern time.

    Attributes:
        timestamp (datetime): The current timestamp.
        is_open (bool): Whether the market is currently open.
        next_open (datetime): The timestamp when the market will next open.
        next_close (datetime): The timestamp when the market will next close.
    """

    timestamp: datetime
    is_open: bool
    next_open: datetime
    next_close: datetime


class Calendar(BaseModel):
    """
    The market calendar for equity markets. Describes the market open and close time on a given day.
    """

    date: date
    open: datetime
    close: datetime

    def __init__(self, **data: Any) -> None:
        """
            Converts open and close time strings from %H:%M to a datetime
        Args:
            **data: The raw calendar data from API
        """
        if "date" in data and "open" in data:
            start_datetime_str = data["date"] + " " + data["open"]
            data["open"] = datetime.strptime(start_datetime_str, "%Y-%m-%d %H:%M")

        if "date" in data and "close" in data:
            start_datetime_str = data["date"] + " " + data["close"]
            data["close"] = datetime.strptime(start_datetime_str, "%Y-%m-%d %H:%M")

        super().__init__(**data)


class BaseActivity(BaseModel):
    """
    Represents Base information for an event/activity for a specific Account.

    You most likely will want an instance of one of the child classes TradeActivity and NonTradeActivity

    Attributes:
        id (str): Unique ID of this Activity. Note that IDs for Activity instances are formatted like
          `20220203000000000::045b3b8d-c566-4bef-b741-2bf598dd6ae7` the first part before the `::` is a date string
          while the part after is a UUID
        account_id (UUID): id of the Account this activity relates too
        activity_type (ActivityType): What specific kind of Activity this was
    """

    id: str
    account_id: UUID
    activity_type: ActivityType

    def __init__(self, *args, **data):
        if "account_id" in data and type(data["account_id"]) == str:
            data["account_id"] = UUID(data["account_id"])

        super().__init__(*args, **data)


class NonTradeActivity(BaseActivity):
    """
    A NonTradeActivity represents an Activity that happened for an account that doesn't have to do with orders or trades.

    Attributes:
        date (date): The date on which the activity occurred or on which the transaction associated with the
          activity settled.
        net_amount (float): The net amount of money (positive or negative) associated with the activity.
        description (str): Extra description of the NTA if needed. Can be empty string ""
        status (NonTradeActivityStatus): Status of the activity. Not present for all activity types.
        symbol (Optional[str]): The symbol of the security involved with the activity. Not present for all activity
          types.
        qty (Optional[float]): For dividend activities, the number of shares that contributed to the payment. Not
          present for other activity types.
        price (Optional[float]) Not present for all activity types.
        per_share_amount (Optional[float]): For dividend activities, the average amount paid per share. Not present for
          other activity types.
    """

    date: date
    net_amount: float
    description: str
    status: Optional[NonTradeActivityStatus] = None
    symbol: Optional[str] = None
    qty: Optional[float] = None
    price: Optional[float] = None
    per_share_amount: Optional[float] = None


class TradeActivity(BaseActivity):
    """
    Represents information for TradeActivities. TradeActivities are Activities that pertain to trades that happened for
    an account. IE Fills or partial fills for orders.

    Attributes:
        transaction_time (datetime): The time and date of when this trade was processed
        type (TradeActivityType): What kind of trade this TradeActivity represents. See TradeActivityType for more
          details
        price (float): The per-share price that the trade was executed at.
        qty (float): The number of shares involved in the trade execution.
        side (OrderSide): What side the trade this TradeActivity represents was on. See OrderSide for more information
        symbol (str): The symbol of the asset that was traded
        leaves_qty (float): For partially filled orders, the quantity of shares that are left to be filled. Will be 0 if
          order was not a partially filled order
        order_id (UUID): The ID for the order filled
        cum_qty (float): The cumulative quantity of shares involved in the execution.
        order_status (OrderStatus): The status of the order that executed the trade. See OrderStatus for more details
    """

    transaction_time: datetime
    type: TradeActivityType
    price: float
    qty: float
    side: OrderSide
    symbol: str
    leaves_qty: float
    order_id: UUID
    cum_qty: float
    order_status: OrderStatus


class TradeAccount(BaseModel):
    """
    Represents trading account information for an Account.

    Attributes:
        id (UUID): The account ID
        account_number (str): The account number
        status (AccountStatus): The current status of the account
        crypto_status (Optional[AccountStatus]): The status of the account in regards to trading crypto. Only present if
          crypto trading is enabled for your brokerage account.
        currency (Optional[str]): Currently will always be the value "USD".
        buying_power (str): Current available cash buying power. If multiplier = 2 then
          buying_power = max(equity-initial_margin(0) * 2). If multiplier = 1 then buying_power = cash.
        regt_buying_power (str): User’s buying power under Regulation T
          (excess equity - (equity - margin value) - * margin multiplier)
        daytrading_buying_power (str): The buying power for day trades for the account
        non_marginable_buying_power (str): The non marginable buying power for the account
        cash (str): Cash balance in the account
        accrued_fees (str): Fees accrued in this account
        pending_transfer_out (Optional[str]): Cash pending transfer out of this account
        pending_transfer_in (Optional[str]): Cash pending transfer into this account
        portfolio_value (str): Total value of cash + holding positions.
          (This field is deprecated. It is equivalent to the equity field.)
        pattern_day_trader (bool): Whether the account is flagged as pattern day trader or not.
        trading_blocked (bool): If true, the account is not allowed to place orders.
        transfers_blocked (bool): If true, the account is not allowed to request money transfers.
        account_blocked (bool): If true, the account activity by user is prohibited.
        created_at (datetime): Timestamp this account was created at
        trade_suspended_by_user (bool): If true, the account is not allowed to place orders.
        multiplier (str): Multiplier value for this account.
        shorting_enabled (bool): Flag to denote whether or not the account is permitted to short
        equity (str): This value is cash + long_market_value + short_market_value. This value isn't calculated in the
          SDK it is computed on the server and we return the raw value here.
        last_equity (str): Equity as of previous trading day at 16:00:00 ET
        long_market_value (str): Real-time MtM value of all long positions held in the account
        short_market_value (str): Real-time MtM value of all short positions held in the account
        initial_margin (str): Reg T initial margin requirement
        maintenance_margin (str): Maintenance margin requirement
        last_maintenance_margin (str): Maintenance margin requirement on the previous trading day
        sma (str): Value of Special Memorandum Account (will be used at a later date to provide additional buying_power)
        daytrade_count (int): The current number of daytrades that have been made in the last 5 trading days
          (inclusive of today)
    """

    id: UUID
    account_number: str
    status: AccountStatus
    crypto_status: Optional[AccountStatus]
    currency: Optional[str]
    buying_power: str
    regt_buying_power: str
    daytrading_buying_power: str
    non_marginable_buying_power: str
    cash: str
    accrued_fees: str
    pending_transfer_out: Optional[str]
    pending_transfer_in: Optional[str]
    portfolio_value: str
    pattern_day_trader: bool
    trading_blocked: bool
    transfers_blocked: bool
    account_blocked: bool
    created_at: datetime
    trade_suspended_by_user: bool
    multiplier: str
    shorting_enabled: bool
    equity: str
    last_equity: str
    long_market_value: str
    short_market_value: str
    initial_margin: str
    maintenance_margin: str
    last_maintenance_margin: str
    sma: str
    daytrade_count: int


class CorporateActionAnnouncement(BaseModel):
    """
    An announcement of a corporate action. Corporate actions are events like dividend payouts, mergers and stock splits.

    Attributes:
        id (UUID): The unique identifier for this single announcement.
        corporate_action_id (str): ID that remains consistent across all announcements for the same corporate action.
        ca_type (CorporateActionType): The type of corporate action that was announced.
        ca_sub_type (CorporateActionSubType): The specific subtype of corporate action that was announced.
        initiating_symbol (str): Symbol of the company initiating the announcement.
        initiating_original_cusip (str): CUSIP of the company initiating the announcement.
        target_symbol (str): Symbol of the child company involved in the announcement.
        target_original_cusip (str): CUSIP of the child company involved in the announcement.
        declaration_date (date): Date the corporate action or subsequent terms update was announced.
        ex_date (date): The first date that purchasing a security will not result in a corporate action entitlement.
        record_date (date): The date an account must hold a settled position in the security in order to receive the
            corporate action entitlement.
        payable_date (date): The date the announcement will take effect. On this date, account stock and cash
            balances are expected to be processed accordingly.
        cash (float): The amount of cash to be paid per share held by an account on the record date.
        old_rate (float): The denominator to determine any quantity change ratios in positions.
        new_rate (float): The numerator to determine any quantity change ratios in positions.
    """

    id: UUID
    corporate_action_id: str
    ca_type: CorporateActionType
    ca_sub_type: CorporateActionSubType
    initiating_symbol: str
    initiating_original_cusip: str
    target_symbol: str
    target_original_cusip: str
    declaration_date: Optional[date]
    ex_date: date
    record_date: date
    payable_date: date
    cash: float
    old_rate: float
    new_rate: float


class TradeUpdate(BaseModel):
    event: Union[TradeEvent, str]
    execution_id: UUID
    order: Order
    timestamp: datetime
    position_qty: Optional[float]
    price: Optional[float]
    qty: Optional[float]
