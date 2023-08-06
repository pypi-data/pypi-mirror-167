from pyteal import *


period_identifier_key = Bytes("period_identifier")
eligible_committed_stake_key = Bytes("eligible_committed_stake")
ineligible_committed_stake_key = Bytes("ineligible_committed_stake")
eligible_governor_count_key = Bytes("eligible_governor_count")
ineligible_governor_count_key = Bytes("ineligible_governor_count")
algo_amount_in_reward_pool_key = Bytes("algo_amount_in_reward_pool")
updated_at_key = Bytes("updated_at")


handle_creation = Seq(
    App.globalPut(period_identifier_key, Int(0)),

    App.globalPut(eligible_committed_stake_key, Int(0)),
    App.globalPut(ineligible_committed_stake_key, Int(0)),

    App.globalPut(eligible_governor_count_key, Int(0)),
    App.globalPut(ineligible_governor_count_key, Int(0)),

    App.globalPut(algo_amount_in_reward_pool_key, Int(0)),

    App.globalPut(updated_at_key, Int(0)),

    Approve()
)


handle_update_and_delete = Seq(
    Assert(Txn.sender() == Global.creator_address()),
)


router = Router(
    # Name of the contract
    name="Algorand Governance Statistics Oracle",
    descr="Statistics related with the current governance period.",

    # What to do for each on-complete type when no arguments are passed (bare call)
    bare_calls=BareCallActions(
        # On create only, just approve
        no_op=OnCompleteAction.create_only(handle_creation),

        # Always let creator update/delete but only by the creator of this contract
        update_application=OnCompleteAction.always(handle_update_and_delete),
        delete_application=OnCompleteAction.always(handle_update_and_delete),

        close_out=OnCompleteAction.never(),
        opt_in=OnCompleteAction.never(),
        clear_state=OnCompleteAction.never(),
    ),
)


@router.method
def update(
        period_identifier: abi.DynamicBytes,
        eligible_committed_stake: abi.Uint64,
        ineligible_committed_stake: abi.Uint64,
        eligible_governor_count: abi.Uint64,
        ineligible_governor_count: abi.Uint64,
        algo_amount_in_reward_pool: abi.Uint64,
        updated_at: abi.Uint64,
    ):
    """
    A single method updates the smart contract global state.
    """

    return Seq(
        Assert(Global.group_size() == Int(1)),
        Assert(Txn.sender() == Global.creator_address()),

        App.globalPut(period_identifier_key, period_identifier.get()),

        App.globalPut(eligible_committed_stake_key, eligible_committed_stake.get()),
        App.globalPut(ineligible_committed_stake_key, ineligible_committed_stake.get()),

        App.globalPut(eligible_governor_count_key, eligible_governor_count.get()),
        App.globalPut(ineligible_governor_count_key, ineligible_governor_count.get()),

        App.globalPut(algo_amount_in_reward_pool_key, algo_amount_in_reward_pool.get()),
        App.globalPut(updated_at_key, updated_at.get()),
    )


approval_program, clear_program, contract = router.compile_program(version=6)
