case_insensitive_keywords = """
K_SELECT:      S E L E C T;
K_FROM:        F R O M;
K_AS:          A S;
K_CAST:        C A S T;
K_WHERE:       W H E R E;
K_AND:         A N D;
K_KEY:         K E Y;
K_KEYS:        K E Y S;
K_ENTRIES:     E N T R I E S;
K_FULL:        F U L L;
K_INSERT:      I N S E R T;
K_UPDATE:      U P D A T E;
K_WITH:        W I T H;
K_LIMIT:       L I M I T;
K_USING:       U S I N G;
K_USE:         U S E;
K_DISTINCT:    D I S T I N C T;
K_COUNT:       C O U N T;
K_SET:         S E T;
K_BEGIN:       B E G I N;
K_UNLOGGED:    U N L O G G E D;
K_BATCH:       B A T C H;
K_APPLY:       A P P L Y;
K_TRUNCATE:    T R U N C A T E;
K_DELETE:      D E L E T E;
K_IN:          I N;
K_CREATE:      C R E A T E;
K_KEYSPACE:    ( K E Y S P A C E
                 | S C H E M A );
K_KEYSPACES:   K E Y S P A C E S;
K_COLUMNFAMILY:( C O L U M N F A M I L Y
                 | T A B L E );
K_MATERIALIZED:M A T E R I A L I Z E D;
K_VIEW:        V I E W;
K_INDEX:       I N D E X;
K_CUSTOM:      C U S T O M;
K_ON:          O N;
K_TO:          T O;
K_DROP:        D R O P;
K_PRIMARY:     P R I M A R Y;
K_INTO:        I N T O;
K_VALUES:      V A L U E S;
K_TIMESTAMP:   T I M E S T A M P;
K_TTL:         T T L;
K_ALTER:       A L T E R;
K_RENAME:      R E N A M E;
K_ADD:         A D D;
K_TYPE:        T Y P E;
K_COMPACT:     C O M P A C T;
K_STORAGE:     S T O R A G E;
K_ORDER:       O R D E R;
K_BY:          B Y;
K_ASC:         A S C;
K_DESC:        D E S C;
K_ALLOW:       A L L O W;
K_FILTERING:   F I L T E R I N G;
K_IF:          I F;
K_IS:          I S;
K_CONTAINS:    C O N T A I N S;

K_GRANT:       G R A N T;
K_ALL:         A L L;
K_PERMISSION:  P E R M I S S I O N;
K_PERMISSIONS: P E R M I S S I O N S;
K_OF:          O F;
K_REVOKE:      R E V O K E;
K_MODIFY:      M O D I F Y;
K_AUTHORIZE:   A U T H O R I Z E;
K_DESCRIBE:    D E S C R I B E;
K_NORECURSIVE: N O R E C U R S I V E;

K_USER:        U S E R;
K_USERS:       U S E R S;
K_ROLE:        R O L E;
K_ROLES:       R O L E S;
K_SUPERUSER:   S U P E R U S E R;
K_NOSUPERUSER: N O S U P E R U S E R;
K_PASSWORD:    P A S S W O R D;
K_LOGIN:       L O G I N;
K_NOLOGIN:     N O L O G I N;
K_OPTIONS:     O P T I O N S;

K_CLUSTERING:  C L U S T E R I N G;
K_ASCII:       A S C I I;
K_BIGINT:      B I G I N T;
K_BLOB:        B L O B;
K_BOOLEAN:     B O O L E A N;
K_COUNTER:     C O U N T E R;
K_DECIMAL:     D E C I M A L;
K_DOUBLE:      D O U B L E;
K_DURATION:    D U R A T I O N;
K_FLOAT:       F L O A T;
K_INET:        I N E T;
K_INT:         I N T;
K_SMALLINT:    S M A L L I N T;
K_TINYINT:     T I N Y I N T;
K_TEXT:        T E X T;
K_UUID:        U U I D;
K_VARCHAR:     V A R C H A R;
K_VARINT:      V A R I N T;
K_TIMEUUID:    T I M E U U I D;
K_TOKEN:       T O K E N;
K_WRITETIME:   W R I T E T I M E;
K_DATE:        D A T E;
K_TIME:        T I M E;

K_NULL:        N U L L;
K_NOT:         N O T;
K_EXISTS:      E X I S T S;

K_MAP:         M A P;
K_LIST:        L I S T;
K_NAN:         N A N;
K_INFINITY:    I N F I N I T Y;
K_TUPLE:       T U P L E;

K_TRIGGER:     T R I G G E R;
K_STATIC:      S T A T I C;
K_FROZEN:      F R O Z E N;

K_FUNCTION:    F U N C T I O N;
K_AGGREGATE:   A G G R E G A T E;
K_SFUNC:       S F U N C;
K_STYPE:       S T Y P E;
K_FINALFUNC:   F I N A L F U N C;
K_INITCOND:    I N I T C O N D;
K_RETURNS:     R E T U R N S;
K_CALLED:      C A L L E D;
K_INPUT:       I N P U T;
K_LANGUAGE:    L A N G U A G E;
K_OR:          O R;
K_REPLACE:     R E P L A C E;
K_JSON:        J S O N;
K_DEFAULT:     D E F A U L T;
K_UNSET:       U N S E T;

K_EMPTY:       E M P T Y;

K_BYPASS:      B Y P A S S;
K_CACHE:       C A C H E;

K_PER:         P E R;
K_PARTITION:   P A R T I T I O N;

K_SERVICE_LEVEL: S E R V I C E '_' L E V E L;
K_ATTACH: A T T A C H;
K_DETACH: D E T A C H;
K_SERVICE_LEVELS: S E R V I C E '_' L E V E L S;
K_ATTACHED: A T T A C H E D;
K_FOR: F O R;
K_SERVICE: S E R V I C E;
K_LEVEL: L E V E L;
K_LEVELS: L E V E L S;

K_SCYLLA_TIMEUUID_LIST_INDEX: S C Y L L A '_' T I M E U U I D '_' L I S T '_' I N D E X;
K_SCYLLA_COUNTER_SHARD_LIST: S C Y L L A '_' C O U N T E R '_' S H A R D '_' L I S T; 
K_SCYLLA_CLUSTERING_BOUND: S C Y L L A '_' C L U S T E R I N G '_' B O U N D;


K_GROUP:       G R O U P;

K_LIKE:        L I K E;

K_TIMEOUT:     T I M E O U T;
K_PRUNE:       P R U N E;
"""


unreserved_keywords = """
unreserved_keyword returns [sstring str]
    : u=unreserved_function_keyword     { $str = u; }
    | k=(K_TTL | K_COUNT | K_WRITETIME | K_KEY) { $str = $k.text; }
    ;

unreserved_function_keyword returns [sstring str]
    : u=basic_unreserved_keyword { $str = u; }
    | t=native_or_internal_type[true]   { $str = t->as_cql3_type().to_string(); }
    ;

basic_unreserved_keyword returns [sstring str]
    : k=( K_KEYS
        | K_AS
        | K_CLUSTERING
        | K_COMPACT
        | K_STORAGE
        | K_TYPE
        | K_VALUES
        | K_MAP
        | K_LIST
        | K_FILTERING
        | K_PERMISSION
        | K_PERMISSIONS
        | K_KEYSPACES
        | K_ALL
        | K_USER
        | K_USERS
        | K_ROLE
        | K_ROLES
        | K_SUPERUSER
        | K_NOSUPERUSER
        | K_LOGIN
        | K_NOLOGIN
        | K_OPTIONS
        | K_PASSWORD
        | K_EXISTS
        | K_CUSTOM
        | K_TRIGGER
        | K_DISTINCT
        | K_CONTAINS
        | K_STATIC
        | K_FROZEN
        | K_TUPLE
        | K_FUNCTION
        | K_AGGREGATE
        | K_SFUNC
        | K_STYPE
        | K_FINALFUNC
        | K_INITCOND
        | K_RETURNS
        | K_LANGUAGE
        | K_CALLED
        | K_INPUT
        | K_JSON
        | K_CACHE
        | K_BYPASS
        | K_LIKE
        | K_PER
        | K_PARTITION
        | K_SERVICE_LEVEL
        | K_ATTACH
        | K_DETACH
        | K_SERVICE_LEVELS
        | K_ATTACHED
        | K_FOR
        | K_GROUP
        | K_TIMEOUT
        | K_SERVICE
        | K_LEVEL
        | K_LEVELS
        | K_PRUNE
        ) { $str = $k.text; }
    ;


native_or_internal_type [bool internal] returns [data_type t]
    : n=native_type     { $t = n; }
    // The "internal" types, only supported when internal==true:
    | K_EMPTY   {
        if (internal) {
            $t = empty_type;
        } else {
            add_recognition_error("Invalid (reserved) user type name empty");
        }
      }
    ;
comparatorType returns [shared_ptr<cql3_type::raw> t]
    : tt=comparator_type[false]    { $t = tt; }
    ;
native_type returns [data_type t]
    : K_ASCII     { $t = ascii_type; }
    | K_BIGINT    { $t = long_type; }
    | K_BLOB      { $t = bytes_type; }
    | K_BOOLEAN   { $t = boolean_type; }
    | K_COUNTER   { $t = counter_type; }
    | K_DECIMAL   { $t = decimal_type; }
    | K_DOUBLE    { $t = double_type; }
    | K_DURATION  { $t = duration_type; }
    | K_FLOAT     { $t = float_type; }
    | K_INET      { $t = inet_addr_type; }
    | K_INT       { $t = int32_type; }
    | K_SMALLINT  { $t = short_type; }
    | K_TEXT      { $t = utf8_type; }
    | K_TIMESTAMP { $t = timestamp_type; }
    | K_TINYINT   { $t = byte_type; }
    | K_UUID      { $t = uuid_type; }
    | K_VARCHAR   { $t = utf8_type; }
    | K_VARINT    { $t = varint_type; }
    | K_TIMEUUID  { $t = timeuuid_type; }
    | K_DATE      { $t = simple_date_type; }
    | K_TIME      { $t = time_type; }
    ;

""" 


host = '127.0.0.1'
port = 9043
