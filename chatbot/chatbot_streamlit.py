def execute_command(command, conn):
    command = command.strip().lower()

    try:
        # ---------------- Show tables ----------------
        if command.startswith("show tables"):
            df = pd.read_sql(
                "SELECT table_name FROM information_schema.tables WHERE table_schema='public';",
                conn
            )
            if df.empty:
                return "No tables found."
            return df

        # ---------------- Show transactions of <customer_id> ----------------
        elif command.startswith("show transactions"):
            parts = command.split()
            if len(parts) < 4:
                return "Usage: show transactions of <customer_id>"

            customer_id = parts[-1]

            df = pd.read_sql(
                f"SELECT * FROM transactions WHERE customer_id = {customer_id};",
                conn
            )

            if df.empty:
                return f"No transactions found for customer_id {customer_id}"

            return df

        # ---------------- Show fraud alerts ----------------
        elif command.startswith("show fraud alerts"):
            df = pd.read_sql(
                "SELECT alert_id, txn_id, customer_id, score, detected_at, alert_type, message "
                "FROM fraud_alerts ORDER BY detected_at DESC;",
                conn
            )

            if df.empty:
                return "No fraud alerts found."

            return df

        # ---------------- Unknown Command ----------------
        else:
            return (
                "Unknown command!\n"
                "Try:\n"
                "- show tables\n"
                "- show transactions of <customer_id>\n"
                "- show fraud alerts"
            )

    except Exception as e:
        return f"Error executing command: {e}"
