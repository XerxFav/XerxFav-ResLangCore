#pragma once

#include <boost/statechart/state_machine.hpp>
#include <boost/statechart/simple_state.hpp>
#include <boost/statechart/transition.hpp>
#include <boost/multiprecision/cpp_int.hpp>

namespace reslang::phase {

using tbit = boost::multiprecision::uint128_t;  // троичный бит
using tbyte = boost::multiprecision::uint256_t; // фазовый байт
using tword = boost::multiprecision::uint512_t; // фазовое слово

// Фазовые состояния
struct PhaseInit;
struct PhaseActive;
struct PhaseMigrating;
struct PhaseFinal;

// Машина состояний
struct PhaseMachine : boost::statechart::state_machine<PhaseMachine, PhaseInit> {};

// Состояния
struct PhaseInit : boost::statechart::simple_state<PhaseInit, PhaseMachine> {};
struct PhaseActive : boost::statechart::simple_state<PhaseActive, PhaseMachine> {};
struct PhaseMigrating : boost::statechart::simple_state<PhaseMigrating, PhaseMachine> {};
struct PhaseFinal : boost::statechart::simple_state<PhaseFinal, PhaseMachine> {};

} // namespace reslang::phase
