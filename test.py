def tally_votes():
    """
    Count votes.

    Players who did not vote are automatically counted as SKIP.

    Returns:
        (eliminated_name, eliminated_id)
        or
        (None, None) if Skip wins or there is a tie.
    """

    # Get all alive players
    alive_players = get_alive_players()

    # Count votes
    vote_counts = {}

    for voter_id, target_name in votes.items():
        vote_counts[target_name] = vote_counts.get(target_name, 0) + 1

    # Players who did not vote = SKIP
    for player_id, player in alive_players:
        if player_id not in votes:
            vote_counts["SKIP"] = vote_counts.get("SKIP", 0) + 1

    # Safety check
    if not vote_counts:
        return None, None

    # Find highest vote count
    max_votes = max(vote_counts.values())

    top_targets = [
        name
        for name, count in vote_counts.items()
        if count == max_votes
    ]

    # Tie
    if len(top_targets) > 1:
        return None, None

    # Skip received the most votes
    if top_targets[0] == "SKIP":
        return None, None

    # A player received the most votes
    eliminated_name = top_targets[0]
    eliminated_id = find_player_id_by_name(eliminated_name)

    return eliminated_name, eliminated_id
